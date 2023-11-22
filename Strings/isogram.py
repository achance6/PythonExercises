def is_isogram(string: str):
    scrubbed = [letter.lower() for letter in string if letter.isalpha()]
    return len(set(scrubbed)) == len(scrubbed)