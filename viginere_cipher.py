from itertools import cycle

ALP_SIZE = 26 # size of alphabet used for modulo

def viginere_cipher(message: str, key: str, encrypt = True) -> str:
    """Encrypts or decrypts a given message using a the viginere cipher with
    a given key.
    :message: message to encrypt/decrypt
    :key: key to use
    :encrypt: True to encrypt, false to decrypt
    :return: encrypted / decrypted message
    """
    key_it = cycle(key.upper())
    trans = ''

    for letter in message:
        # adds spaces from original input to output
        trans += (v_cipher_letter(letter, next(key_it), encrypt) 
                  if letter.isalpha() else letter)
    return trans

def v_cipher_letter(letter: str, key_letter: str, encrypt = True) -> str:
    """Returns the encrypted or decrypted letter using viginere cipher.
    :letter: letter to encrypt/decrypt
    :key_letter: key letter to use
    :encrypt: True to encrypt, False to decrypt
    :return: encrypted or decrypted letter
    """
    if not letter.isalpha(): return letter

    # squishes letter 0-25
    if letter.islower():
        if encrypt:
            squished_letter = (((ord(letter) - ord('a')) + 
                                (ord(key_letter) - ord('A'))) 
                                % ALP_SIZE)
        else:
            squished_letter = (((ord(letter) - ord('a')) - 
                                (ord(key_letter) - ord('A'))) 
                                % ALP_SIZE)
        return chr(squished_letter + ord('a'))
    else:
        if encrypt:
            squished_letter = (((ord(letter) - ord('A')) + 
                                (ord(key_letter) - ord('A'))) 
                                % ALP_SIZE)
        else:
            squished_letter = (((ord(letter) - ord('A')) - 
                                (ord(key_letter) - ord('A'))) 
                                % ALP_SIZE)

    return chr(squished_letter + ord('A'))


# print(viginere_cipher('HELLO WORLD', 'KEY', encrypt = True))
# print(viginere_cipher('K op ep VWQN Dusifdqosu', 'CODE', encrypt = False))
