# Prompts user for radius, computes area of circle and volume of sphere
# with radius r

import math 

r = float(input("Input radius: "))
area = math.pi * (r ** 2)
volume = (4 / 3 * math.pi) * (r ** 3)
print("Area is %.2f and volume is %.2f" % (area, volume))