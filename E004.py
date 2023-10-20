#Asks user for width and length, computes amount of acres in area
width = float(input("Width in feet: "))
length = float(input("Length in feet: "))
FEETINACRE = 43_560
acres = (width * length) / FEETINACRE
print("Area in acres is", "%.2f" % (acres))