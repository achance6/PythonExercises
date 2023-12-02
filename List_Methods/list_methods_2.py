from enum import Enum

class Color(Enum):
    BLACK = 0
    BROWN = 1
    RED = 2
    ORANGE = 3
    YELLOW = 4
    GREEN = 5
    BLUE = 6
    VIOLET = 7
    GREY = 8
    WHITE = 9

def label(colors: list[str]) -> str:
    colors = [color.upper() for color in colors]
    ohms = (10 * Color[colors[0]].value + Color[colors[1]].value) * (10 ** Color[colors[2]].value)
    
    prefix = ''
    if ohms >= 1_000_000_000:
        prefix = 'giga'
        ohms = round(ohms / 1_000_000_000)
    elif ohms >= 1_000_000:
        prefix = 'mega'
        ohms = round(ohms / 1_000_000)
    elif ohms >= 1_000:
        prefix = 'kilo'
        ohms = round(ohms / 1_000)
    
    return f'{ohms} {prefix}ohms'

# print(label(['Blue', 'Grey', 'Brown']))
# print(label(['blue', 'violet', 'blue']))
# print(label(['black', 'black', 'black']))
