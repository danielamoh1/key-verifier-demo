# key-verifier-demo
Proof of private key ownership using Flask and RSA signatures

# Private Key Ownership Verifier Demo

This project demonstrates proof of private key ownership using a Flask-based web service and a holder script that signs a message with a private key.

## Prerequisites
- Python 3.10+
- pip installed
- Internet connection
- Flask and Cryptography libraries (pip install flask cryptography requests)

##  Components
| File | Description |
|------|--------------|
| generate_keys.py | Generates RSA public/private key pair |
| verifier.py | Flask API that provides a nonce and verifies signatures |
| holder.py | Client script that signs a message + nonce and proves key ownership |


## How to Run the Demo ##

### 1. Generate Keys
python generate_keys.py

Two files are created:

private_key.pem

public_key.pem


2. Start the Verifier

python verifier.py or python3 verifier.py 

You should see:

* Running on http://127.0.0.1:5000 (and "http://127.0.0.1:5000/nonce" to see data)

3. Run the Holder Script

In a second terminal:

python holder.py or python3 holder.py

Output:

{"verified": true}


- How It Works

1. The Verifier issues a random nonce.


2. The Holder signs the message + nonce using its private key.


3. The Verifier checks the signature using the public key.


4. Nonces cannot be reused — preventing replay attacks.


Notes

Keys use RSA 2048-bit.

Nonce generation uses 128-bit random values.

Verification uses SHA-256 hashing.
