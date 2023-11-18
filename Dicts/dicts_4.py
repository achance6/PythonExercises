import re
import string

def count_words(sentence: str) -> dict[str, int]:
    # won't work if literal placed in f string below due to parsing errors
    apost = "'" 
    expr = re.compile(f'[{string.punctuation.replace(apost, "")}]\\s*|\\s+?')
    
    words = [word.lower().strip("'\"") 
             for word in re.split(expr, sentence) 
             if word.strip("'\"")]
    
    res = {}
    for word in words:
        res[word] = res.get(word, 0) + 1
    return res

# print(count_words("'First: don't laugh. Then: don't cry. You're getting it.'"))
