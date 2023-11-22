from enum import Enum

def value(colors: list):
    colors = colors[:2]
    res = ""
    for color in colors:
        res += str(color_code(color))
    return int(res)

def color_code(color: str):
    return Color[color.upper()].value

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