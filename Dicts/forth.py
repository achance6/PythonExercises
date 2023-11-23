import re
import string as s

WORDS = ['+', '-', '*', '/', 'DUP', 'DROP', 'SWAP', 'OVER']
VAR_MATCH = re.compile(f'[a-zA-Z{s.punctuation}\d\W]+')

class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message: str):
        self.message = message


def evaluate(input_data: str) -> list[int]:
    input_list = input_data.split()
    stack = []
    for token in input_list:
        validate(token)
        stack.append(int(token)) if token.isdigit() else stack.append(token)

    while (len(stack) > 0):
        token = stack.pop()
        match token:
            case '+':
                try:
                    num1 = stack.pop()
                    num2 = stack.pop()
                except: raise StackUnderflowError('Insufficient number of items in stack')
                stack.append(num1 + num2)
            case '-':
                try:
                    num1 = stack.pop()
                    num2 = stack.pop()
                except: raise StackUnderflowError('Insufficient number of items in stack')
                stack.append(num1 - num2)
            case '*':
                try:
                    num1 = stack.pop()
                    num2 = stack.pop()
                except: raise StackUnderflowError('Insufficient number of items in stack')
                stack.append(num1 * num2)
            case '/':
                try:
                    num1 = stack.pop()
                    num2 = stack.pop()
                except: raise StackUnderflowError('Insufficient number of items in stack')
                if num2 == 0:
                    raise ZeroDivisionError('divide by zero')
                stack.append(num1 / num2)
    
    return stack

def validate(token: str):
    if re.match(VAR_MATCH, token) is None:
        try:
            WORDS.index(token)
        except:
            raise ValueError('undefined operation')


print(evaluate('1 2 +'))