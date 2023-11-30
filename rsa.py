import random
import math

def get_factors(n: int) -> list[int]:
    """Returns list of factors of given number"""
    factors = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                factors.append(i)
                n = int(n / i) # should always be integer division
                break
            
    return factors

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Extended Euclidean Algorithm to find modular inverse."""
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inv(a: int, m: int) -> int:
    """Modular Multiplicative Inverse."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    else:
        return x % m
    
def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    # factors only need to be checked up to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def create_keys(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Generates public and private keys"""
    n = p * q
    phi = (p - 1) * (q - 1)

    # public key where 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # private key where d * e ≡ 1 (mod phi)
    d = mod_inv(e, phi)

    return ((n, e), (n, d))

def encrypt(message: str, public_key: tuple[int, int]) -> str:
    """Encrypt a message with RSA."""
    n, e = public_key
    ciphertext = str(pow(int(message), e, n))
    return ciphertext

def decrypt(ciphertext: str, private_key: tuple[int, int]) -> str:
    """Decrypt a message with RSA."""
    n, d = private_key
    decrypted_message = str(pow(int(ciphertext), d, n))
    return decrypted_message


# message = '911'
# p, q = (61, 53)
# p, q = get_factors(8051)
# public_key, private_key = create_keys(p, q)
# public_key = (3233, 667)
# private_key = (3233, 1843)
# print(f'public key: {public_key}')
# print(f'private key: {private_key}')
# encrypted_message = encrypt(message, public_key)
# decrypted_message = decrypt(encrypted_message, private_key)

# print(f'Original message: {message}')
# print(f'Encrypted message: {encrypted_message}')
# print(f'Decrypted message: {decrypted_message}')