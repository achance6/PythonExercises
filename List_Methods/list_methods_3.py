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

GIGA_THR = 1_000_000_000
MEGA_THR = 1_000_000
KILO_THR = 1_000

def resistor_label(colors: list[str]) -> str:
    if len(colors) == 1: return '0 ohms'

    # So that upper doesn't need to be called everytime 
    # a value is gotten from enums
    colors = [color.upper() for color in colors]

    v_1 = Color[colors[0]].value if len(colors) > 0 else None
    v_2 = Color[colors[1]].value if len(colors) > 1 else None
    if len(colors) == 3:
        mult = Color[colors[2]].value
        tol = 0
    elif len(colors) == 4:
        mult = Color[colors[2]].value
        tol = Tolerance_Color[colors[3]].value
    elif len(colors) == 5:
        v_3 = Color[colors[2]].value
        mult = Color[colors[3]].value
        tol = Tolerance_Color[colors[4]].value
    else:
        mult = 1
        tol = 0
    
    if len(colors) == 3 or len(colors) == 4:
        ohms = ((10 * v_1) + v_2) * (10 ** mult)
    elif len(colors) == 5:
        ohms = ((100 * v_1) + (10 * v_2) + v_3) * (10 ** mult)
    
    prefix, ohms = apply_ohm_prefix(ohms)
    # Convert back to int if no data loss
    if int(ohms) == ohms: ohms = int(ohms)

    return f'{ohms} {prefix}ohms ±{tol}%'

def apply_ohm_prefix(ohms: int, precision: int = 2) -> tuple[str, int | float]:
    prefix = ''

    if ohms >= GIGA_THR:
        prefix = 'giga'
        ohms = round(ohms / GIGA_THR, precision)
    elif ohms >= MEGA_THR:
        prefix = 'mega'
        ohms = round(ohms / MEGA_THR, precision)
    elif ohms >= KILO_THR:
        prefix = 'kilo'
        ohms = round(ohms / KILO_THR, precision)
    return (prefix, ohms)

assert(resistor_label(['Blue', 'Grey', 'Brown']) == '680 ohms ±0%')
assert(resistor_label(['blue', 'violet', 'blue']) == '67 megaohms ±0%')
assert(resistor_label(['black', 'black', 'black']) == '0 ohms ±0%')
assert(resistor_label(['orange', 'orange', 'brown', 'green']) == '330 ohms ±0.5%')
assert(resistor_label(['orange', 'orange', 'blue', 'red']) == '33 megaohms ±2%')
assert(resistor_label(["red", "green", "yellow", "yellow", "brown"]) == '2.54 megaohms ±1%')