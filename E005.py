# Asks user for number of small and large containers. 
# Prints the refund they'd get if they recycled them
# where small containers are $0.1 each and large ones are $0.25
smalls = int(input("Amount of small containers: "))
larges = int(input("Amount of large containers: "))
refund = (smalls * 0.1) + (larges * 0.25)
print("Total refund for containers is", "$%.2f" % (refund))