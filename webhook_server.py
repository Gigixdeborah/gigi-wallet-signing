from flask import Flask, request, jsonify
import hmac
import hashlib
import os

app = Flask(__name__)

SECRET = os.environ.get("WEBHOOK_SECRET", "devsecret")

def sign_payload(data: bytes) -> str:
    return hmac.new(SECRET.encode(), data, hashlib.sha256).hexdigest()

@app.route('/generate-signature', methods=['POST'])
def generate_signature():
    signature = sign_payload(request.data)
    return jsonify({'signature': signature})

@app.route('/ton-webhook', methods=['POST'])
@app.route('/evm-webhook', methods=['POST'])
@app.route('/solana-webhook', methods=['POST'])
def handle_webhook():
    print(f"Received {request.path}:", request.json)
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
