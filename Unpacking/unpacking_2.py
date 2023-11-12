def proverb(*words: str, qualifier: str = None) -> str:
    """Generates the 'for want of a nail' proverb using variable arguments"""
    res = []
    if len(words) == 0: return res

    for i in range(len(words) - 1):
        res.append(f'For want of a {words[i]} the {words[i + 1]} was lost.')

    if qualifier is not None:
        res.append(f'And all for the want of a {qualifier} {words[0]}.')
    else: res.append(f'And all for the want of a {words[0]}.')

    return res

# input = ["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"]
# modern = ['pin', 'gun', 'soldier', 'battle']
# for line in proverb(*input):
#     print(line)
# for line in proverb(*modern, qualifier='damned'):
#     print(line)