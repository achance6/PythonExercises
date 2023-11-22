import math

def classify(num: int):
    """ A perfect number equals the sum of its positive divisors.

    :param num: int a positive integer
    :return: str the classification of the input integer
    """
    if num < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if aliquot_sum(num) > num:
        return "abundant"
    if aliquot_sum(num) < num:
        return "deficient"
    return "perfect"

def aliquot_sum(num: int):
    """ Computes sum of factors of a number

    :param num: int a positive integer
    :return: sum of number's factors
    """
    sum = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            sum += i
    return sum

print(classify(0))