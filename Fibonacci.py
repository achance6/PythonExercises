a, b = 0, 1
while a < 10:
    print(a, end=", ") # ends with ", " instead of \n
    a, b = b, a + b # all expressions evaluated before any assignment