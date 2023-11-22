WORDS = ['+', '-', '*', '/', 'DUP', 'DROP', 'SWAP', 'OVER']

class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message: str):
        self.message = message


def evaluate(input_data: str) -> list[int]:
    input_list = input_data.split()
    for token in input_list:
        validate(token)

    stack = []
    
    return stack

def validate(token: str):
    try:
        WORDS.index(token)
    except:
        raise ValueError('undefined operation')

