import math

def score(x, y):
    dist = math.sqrt(x ** 2 + y ** 2)
    if -1 <= dist <= 1 and -1 <= dist <= 1:
        return 10
    if -5 <= dist <= 5 and -5 <= dist <= 5:
        return 5
    if -10 <= dist <= 10 or -10 <= dist <= 10:
        return 1
    return 0
