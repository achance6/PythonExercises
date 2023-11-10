class Luhn:
    """Class representing the Luhn algorithm"""
    def __init__(self, card_num: str) -> None:
        self.isValid = Luhn.check_valid(card_num)

    def valid(self) -> bool:
        return self.isValid
        
    @staticmethod
    def check_valid(card_num: str) -> bool:
        try:
            check_num = [int(num) for num in card_num if not num.isspace()]
        except ValueError: 
            return False
        
        if len(check_num) <= 1:
            return False

        for i in range(len(check_num) - 2, -1, -2):
            check_num[i] = res - 9 if (res := 2 * check_num[i]) > 9 else res

        return sum(check_num) % 10 == 0


# test = Luhn("4539 3195 0343 6467")
# print(test.valid())