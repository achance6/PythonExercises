from enum import Enum

class Color(Enum):
    BLACK  = 0
    BROWN  = 1
    RED    = 2
    ORANGE = 3
    YELLOW = 4
    GREEN  = 5
    BLUE   = 6
    VIOLET = 7
    GREY   = 8
    WHITE  = 9

class Tolerance_Color(Enum):
    GREY   = 0.05
    VIOLET = 0.1
    BLUE   = 0.25
    GREEN  = 0.5
    BROWN  = 1
    RED    = 2
    GOLD   = 5
    SILVER = 10


def resistor_label(colors: list[str]) -> str:
    if len(colors) == 1: return '0 ohms'

    colors = [color.upper() for color in colors]

    v_1 = Color[colors[0]].value if len(colors) > 0 else None
    v_2 = Color[colors[1]].value if len(colors) > 1 else None
    v_3 = Color[colors[2]].value if len(colors) == 5 else None
    if len(colors) == 3:
        mult = Color[colors[2]].value
        tol = 0
    elif len(colors) == 4:
        mult = Color[colors[2]].value
        tol = Tolerance_Color[colors[3]].value
    elif len(colors) == 5:
        mult = Color[colors[3]].value
        tol = Tolerance_Color[colors[4]].value
    else:
        mult = 1
        tol = 0
    
    if len(colors) == 3 or len(colors) == 4:
        ohms = ((10 * v_1) + v_2) * (10 ** mult)
    elif len(colors) == 5:
        ohms = ((100 * v_1) + (10 * v_2) + v_3) * (10 ** mult)
    
    prefix, ohms = ohm_prefix(ohms)
    if int(ohms) == ohms: ohms = int(ohms)

    return f'{ohms} {prefix}ohms ±{tol}%'

def ohm_prefix(ohms: int) -> tuple[str, int]:
    prefix = ''
    if ohms >= 1_000_000_000:
        prefix = 'giga'
        ohms = round(ohms / 1_000_000_000, 2)
    elif ohms >= 1_000_000:
        prefix = 'mega'
        ohms = round(ohms / 1_000_000, 2)
    elif ohms >= 1_000:
        prefix = 'kilo'
        ohms = round(ohms / 1_000, 2)
    return (prefix, ohms)

# print(resistor_label(['Blue', 'Grey', 'Brown']))
# print(resistor_label(['blue', 'violet', 'blue']))
# print(resistor_label(['black', 'black', 'black']))
# print(resistor_label(['orange', 'orange', 'brown', 'green']))
# print(resistor_label(['orange', 'orange', 'blue', 'red']))
# print(resistor_label(["red", "green", "yellow", "yellow", "brown"]))