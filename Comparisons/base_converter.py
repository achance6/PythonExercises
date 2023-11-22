def rebase(input_base: int, digits: list, output_base: int) -> list:
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if len(digits) == 0:
        return [0]
    decimal = to_decimal(input_base, digits)
    output = []
    while True: # conversion to output base, do while loop
        output.insert(0, decimal % output_base)
        decimal = decimal // output_base
        if decimal == 0:
            break
    return output

def to_decimal(input_base: int, digits: list) -> int:
    decimal = 0
    for index, digit in enumerate(digits):
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        decimal += digit * (input_base ** (len(digits) - 1 - index))
    return decimal
    
print(rebase(2, [1, 0, 1, 1], 10))