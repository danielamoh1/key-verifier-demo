from flask import Flask, request, jsonify
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64, os, time

app = Flask(__name__)
NONCES = set()

with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

@app.route("/nonce", methods=["GET"])
def get_nonce():
    nonce = base64.urlsafe_b64encode(os.urandom(16)).decode()
    NONCES.add(nonce)
    return jsonify({"nonce": nonce})

@app.route("/verify", methods=["POST"])
def verify_signature():
    data = request.get_json()
    message = data.get("message")
    nonce = data.get("nonce")
    signature = base64.b64decode(data.get("signature"))

    if nonce not in NONCES:
        return jsonify({"verified": False, "error": "Invalid or reused nonce"}), 400
    NONCES.remove(nonce)

    try:
        public_key.verify(
            signature,
            (message + nonce).encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return jsonify({"verified": True})
    except Exception as e:
        return jsonify({"verified": False, "error": str(e)}), 400

if __name__ == "__main__":
    app.run(port=5000)