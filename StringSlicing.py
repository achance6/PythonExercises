string = "The red fox jumped over the brown dog"
print(string[0: 3]) # prints "The"
print(string[4:8]) # prints "red"
print(string[: 8]) # prints "The red"
print(string[4:]) # prints "red fox jumped over the brown dog"
print(string[-3:]) # prints "dog"
print(string[:5] + string[5:]) # prints the whole sentence