from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="public")

@app.route("/")
def index():
    return "<h1>Gigi Wallet Signing Server is Live!</h1>"

@app.route("/<path:filename>")
def serve_file(filename):
    return send_from_directory("public", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
