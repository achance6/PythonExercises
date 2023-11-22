import math

#Reads two integers, does some arithmetic and prints results
a = int(input("First integer: "))
b = int(input("Second integer: "))
print("Sum of %d and %d is %d" % (a, b, a + b))
print("Difference of %d and %d is %d" % (a, b, a - b))
print("Product of %d and %d is %d" % (a, b, a * b))
print("Quotient of %d divided by %d is %.2f" % (a, b, a / b))
print("Remainder of %d divided by %d is %d" % (a, b, a % b))
print("Result of log base 10 %d is %.2f" % (a, math.log10(a)))
print("Result of %d to the power of %d is %d" % (a, b, a ** b))