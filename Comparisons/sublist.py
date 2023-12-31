SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def sublist(list_one: list, list_two: list) -> int:
    if list_one == list_two:
        return EQUAL
    if len(list_one) > len(list_two):
        for i in range(len(list_one) - len(list_two) + 1):
            if list_one[i:i + len(list_two)] == list_two:
                return SUPERLIST
    if len(list_one) < len(list_two):
        for i in range(len(list_two) - len(list_one) + 1):
            if list_two[i:i + len(list_one)] == list_one:
                return SUBLIST
    return UNEQUAL
