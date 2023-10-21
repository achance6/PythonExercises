# Prompts user for two points on earth, computes orthodromic distance
# between the two points and prints it

import math as m

EARTH_AVG_RADIUS = 6371.01
x1 = m.radians(float(input("Input latitude of first spot: ")))
y1 = m.radians(float(input("Input longitude of first spot: ")))
x2 = m.radians(float(input("Input latitude of second spot: ")))
y2 = m.radians(float(input("Input longitude of second spot: ")))
distance = (EARTH_AVG_RADIUS * m.acos(
                    m.sin(x1) * m.sin(x2) + 
                    m.cos(x1) * m.cos(x2) * 
                    m.cos(y1 - y2)))
print("Orthodromic Distance between these two points on Earth is %.2fkm" % distance)
