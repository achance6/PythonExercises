# Prompts user for mass of water in grams and temperature change
# Calculates energy required for change and cost in electricity

WATER_SHC = 4.186
COST_KWH = 8.9
JOULES_PER_KWH = 3600000
mass = float(input("Enter mass of water in grams: "))
deltaT = float(input("Enter change in temperature in celsius: "))
joules = mass * WATER_SHC * deltaT
cost = (joules / JOULES_PER_KWH) * COST_KWH
print("Amount of energy required is %.2fJ" % (joules))
print("Cost of electricity is $%.2f" % (cost))
