def rotate(text: str, key: int):
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
    return ciphertext