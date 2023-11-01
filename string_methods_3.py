import string

### Parse and evaluate simple math word problems returning the answer as an integer. ###
def answer(question: str) -> int:
    ops = ['plus', 'minus']
    tokens = [word for word in question.strip(string.punctuation).split() 
            if word.lstrip('-').isdigit() or word in ops]
    tokens.reverse()
    if len(tokens) == 1 and tokens[0].lstrip('-').isdigit():
        return int(tokens[0])
    num1 = int(tokens.pop())
    while len(tokens) > 0:
        op = tokens.pop()
        num2 = int(tokens.pop())
        if op == 'plus':
            num1 += num2
        elif op == 'minus':
            num1 -= num2
    return num1
        
print(answer('What is 5 plus 5 plus 5 minus 3?'))