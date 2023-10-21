# Prompts user for feet and inches, converts to centimeters
CM_PER_FOOT = 30.48
CM_PER_INCH = 2.54
feet = int(input("Enter feet component of height: "))
inches = int(input("Enter inches component of height: "))
cm = feet * CM_PER_FOOT + inches * CM_PER_INCH
print("Height in cenimeters is %.2fcm" % (cm))