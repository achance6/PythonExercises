from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import time

def encrypt(data: bytes, key: bytes) -> tuple[bytes, bytes, bytes]:
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    nonce = cipher.nonce

    return (ciphertext, tag, nonce)

def decrypt(data: bytes, key: bytes, tag: bytes, nonce: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    return cipher.decrypt_and_verify(data, tag)


# with open('bigbook.txt', 'rb') as file_in:
#     message = file_in.read()
# start_time = time.time()

# message = b"Unsecured message"


# key_len = 16
# key = get_random_bytes(key_len)
# ciphertext, tag, nonce = encrypt(message, key)
# encoded = base64.b64encode(ciphertext)
# plaintext = decrypt(base64.b64decode(encoded), key, tag, nonce)

# print(f'Original message is {message.decode()}')
# print(f'Encoded message is {encoded.decode()}')
# print(f'Decoded message is {plaintext.decode()}')

# encrypt_decrypt_time = time.time() - start_time

# with open('out.txt', 'wb') as file_out:
#     file_out.write(plaintext)

# with open('log.txt', 'a') as log:
#     log.write(f'key length of {key_len}:{encrypt_decrypt_time * 1000:.2f}ms\n')
