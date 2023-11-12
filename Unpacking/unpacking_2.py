def proverb(*words: str, qualifier: str = None) -> str:
    """Generates the 'for want of a nail' proverb using variable arguments"""

    res = [f'For want of a {words[i]} the {words[i + 1]} was lost.' 
           for i in range(len(words) - 1)]
    if len(words) == 0: return res

    if len(words) > 0:
        last = words[0] if qualifier is None else f'{qualifier} {words[0]}'
        res.append(f'And all for the want of a {last}.')
    
    return res


input = ["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"]
modern = ['pin', 'gun', 'soldier', 'battle']
for line in proverb(*input):
    print(line)
for line in proverb(*modern, qualifier='damned'):
    print(line)