def square(number: int) -> int:
    if not 1 <= number <= 64:
        raise ValueError('square must be between 1 and 64')
    return 2 ** (number - 1)


def total() -> int:
    return (1 << 64) - 1

def is_armstrong_number(number: int) -> bool:
    # sums digits to the power of number of digits in number and checks if this equals the number
    return sum([int(digit) ** len(str(number)) for digit in str(number)]) == number

# Collatz Conjecture
def steps(number: int) -> int:
    if number < 1:
        raise ValueError('Only positive integers are allowed')
    steps = 0
    while number != 1:
        number = number / 2 if number % 2 == 0 else (number * 3) + 1
        steps += 1
    return steps


print(steps(16))