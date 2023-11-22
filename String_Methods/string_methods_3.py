### Parse and evaluate simple math word problems returning the answer as an integer. ###

import string

def answer(question: str) -> int:
    OPS = ['plus', 'minus', 'divided', 'multiplied']
    tokens = [word for word in question.strip(string.punctuation).split() 
            if word.lstrip('-').isdigit() or word in OPS]
    tokens.reverse()
    if len(tokens) == 0 or len(tokens) % 2 != 1:
        raise ValueError('syntax error')
    if len(tokens) == 1 and tokens[0].lstrip('-').isdigit():
        return int(tokens[0])
    
    check_dig(tokens[-1])
    num1 = int(tokens.pop())
    while len(tokens) > 0:
        op = tokens.pop()
        check_dig(tokens[-1])
        num2 = int(tokens.pop())
        if op == 'plus':
            num1 += num2
        elif op == 'minus':
            num1 -= num2
        elif op == 'multiplied':
            num1 *= num2
        elif op == 'divided':
            if num2 == 0:
                raise ValueError('divide by zero')
            num1 /= num2
    return num1
        
def check_dig(num: str) -> bool:
    if not num.lstrip('-').isdigit():
        raise ValueError('syntax error')
    return True

print(answer('What is 5 plus 5 plus 5 minus 3 multiplied by 4 divided by 4 plus 3?'))