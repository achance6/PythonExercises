# Prompts user for feet, prints equivalent inches, yards, miles
INCHES_PER_FOOT = 12
YARDS_PER_FOOT = 1 / 3
MILES_PER_FOOT = 1 / 5280
feet = int(input("measurement in feet: "))
print("Equivalent inches: %.2f, yards: %.2f, miles: %.3f" % 
      (feet * INCHES_PER_FOOT, feet * YARDS_PER_FOOT, feet * MILES_PER_FOOT))
