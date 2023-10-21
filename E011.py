# Converts user input miles per gallon to liters per hundred kilometers
# and prints result
mpg = float(input("Input MPG: "))
MPG_TO_LPHK = 235.212
print("Liters per 100 kilometers: %.2f" % (mpg * MPG_TO_LPHK))