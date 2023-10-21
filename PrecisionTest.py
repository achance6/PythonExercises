import math

a = 5.25 * 5.25
b = 27.8625
print(a)
print(b)
print(a - b == -0.3) # should be true, is false
print(math.isclose(a - b, -0.3)) # correctly evaluates to true