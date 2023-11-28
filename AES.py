from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt(data: bytes, key: bytes) -> tuple[bytes, bytes, bytes]:
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    nonce = cipher.nonce

    return (ciphertext, tag, nonce)

def decrypt(data: bytes, key: bytes, tag: bytes, nonce: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    return cipher.decrypt_and_verify(data, tag)

key = get_random_bytes(16)
message = 'Unsecured Message'
ciphertext, tag, nonce = encrypt(message.encode(), key)

encoded = base64.b64encode(ciphertext)

print(encoded)
print(decrypt(base64.b64decode(encoded), key, tag, nonce).decode())
