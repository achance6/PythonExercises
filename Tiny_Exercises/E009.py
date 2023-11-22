# Computes compound interest after 1,2,3 compoundings
RATE = 1.04 #4 percent 
msg = "Amount of money to compound at 4" + str(chr(37)) + " annually: $" #can't escape % sign
amount = float(input(msg))
print("After 1 year:", "$%.2f" % (amount * RATE))
print("After 2 years:", "$%.2f" % (amount * (RATE ** 2)))
print("After 3 years:", "$%.2f" % (amount * (RATE ** 3)))