def is_valid(isbn: str):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    sum = 0
    for (index, char) in enumerate(isbn):
        if char.isdigit():
            sum += int(char) * (10 - index)
        elif index == 9 and char.lower() == 'x':
            sum += 10
        else:
            return False
    return sum % 11 == 0

#print(is_valid("1934-425-a-20"))
#print(is_valid("1934-425-20"))
print(is_valid("3-598-21508-8"))
print(is_valid("3-598-21507-X"))