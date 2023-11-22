# Asks user for price of meal. Prints tax and tip
cost = float(input("Cost of meal: $"))
tax = cost * 0.06
tip = cost * 0.18
print("Tax is:", "$%.2f" % (tax))
print("Tip is:", "$%.2f" % (tip))
print("Total cost is", "$%.2f" % (tax + tip + cost))