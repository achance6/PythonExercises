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

def color_code(color: str):
    return Color[color.upper()].value


def colors():
    color_list = []
    for color in list(Color):
        color_list.append(color.name.lower())
    return color_list


