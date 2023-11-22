import string

def is_pangram(sentence: str):
    return all(letter in sentence.lower() for letter in string.ascii_lowercase)
    
print(is_pangram("The quick brown fox jumps over the lazy dog."))