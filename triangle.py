def equilateral(sides: list[float | int]) -> bool:
    """ determines if triangle with given sides is equilateral """
    return is_triangle(sides) and sides[0] == sides[1] == sides[2] 


def isosceles(sides: list[float | int]) -> bool:
    """ determines if triangle with given sides is isoceles """
    return is_triangle(sides) and (sides[0] == sides[1] or 
                                   sides[1] == sides[2] or 
                                   sides[0] == sides[2])


def scalene(sides: list[float | int]) -> bool:
    """ determines if triangle with given sides is scalene """
    return is_triangle(sides) and (sides[0] != sides[1] and 
                                   sides[1] != sides[2] and 
                                   sides[0] != sides[2])

def is_triangle(sides: list[float | int]) -> bool:
    """ determines if triangle with given sides is in fact a triangle"""
    for side in sides:
        if side <= 0:
            return False
    if (sides[0] + sides[1] < sides[2] or 
        sides[1] + sides[2] < sides[0] or
        sides[2] + sides[0] < sides[1]):
        return False
    return True
