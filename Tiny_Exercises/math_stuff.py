def gcd(a, b):
    while b != 0:
        rem = a % b
        a = b
        b = rem
    return a

def coprime(a, b):
    if gcd(a, b) == 1:
        return True