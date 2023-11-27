def rotate(text: str, key: int, preserve = False):
    if not 0 < key < 26:
        key = key % 26
    ciphertext = ""
    for letter in text:
        if letter.isalpha():
            if letter.islower():
                ciphertext += chr((((ord(letter) + key) - ord('a')) % 26) + ord('a'))
            else:
                ciphertext += chr((((ord(letter) + key) - ord('A')) % 26) + ord('A'))
        else:
            ciphertext += letter
    if not preserve:
        ciphertext = ciphertext.replace(' ', '').upper()
        ciphertext = ' '.join([ciphertext[i:i + 5] for i in range(0, len(ciphertext), 5)])
    return ciphertext

# print(rotate('Arminius and his Germanic allies are easily defeatable. Surely nothing will go wrong in Teutoberg forest', 13, preserve=False))
# print(rotate('NEZVA VHFNA QUVFT REZNA VPNYY VRFNE RRNFV YLQRS RNGNO YR.FH ERYLA BGUVA TJVYY TBJEB ATVAG RHGBO RETSB ERFG', -13))