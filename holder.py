import requests, base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# Load your private key
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Step 1: Ask the verifier for a nonce
print("Requesting nonce from verifier...")
r = requests.get("http://127.0.0.1:5000/nonce")
print("Verifier responded with:", r.text)
nonce = r.json()["nonce"]

# Step 2: Sign the message + nonce
message = "I am the holder of this key"
signature = private_key.sign(
    (message + nonce).encode(),
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Step 3: Send message, nonce, and signature to verifier
payload = {
    "message": message,
    "nonce": nonce,
    "signature": base64.b64encode(signature).decode()
}

print("Sending signed payload for verification...")
r = requests.post("http://127.0.0.1:5000/verify", json=payload)
print("Verifier responded with:", r.text)