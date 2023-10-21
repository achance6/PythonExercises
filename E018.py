# Computes volume of a cylinder
import math

r = float(input("Input radius: "))
h = float(input("Input height: "))
v = (math.pi * (r ** 2)) * h
print("Volume of cylinder is %.1f" % (v))