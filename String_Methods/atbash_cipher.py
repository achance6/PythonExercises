"""Implements atbash cipher, an encryption method that 
simply uses the reverse alphabet to encode text"""

import string

# Reverse string, remove punctuation
CIPHER = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])

def encode(plain_text: str) -> str:
    """Encode a string using atbash cipher"""
    cipher_text = ''.join([chr for chr in plain_text.lower() if chr.isalnum()]).translate(CIPHER)
    # break string into groups of 5 characters
    return ' '.join([cipher_text[i:i + 5] for i in range(0, len(cipher_text), 5)])
    
def decode(ciphered_text: str) -> str:
    """Decode a string that's been encoded with the atbash cipher"""
    return ''.join([chr for chr in ciphered_text.lower() if chr.isalnum()]).translate(CIPHER)