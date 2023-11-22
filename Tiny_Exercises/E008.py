# Widgets weigh 75g, gizmos weight 112g
# program asks users for amount of widgets and gizmos,
# prints total weight

widgets = int(input("Widgets: "))
gizmos = int(input("Gizmos: "))
print("Total weight of parts is", "%ig" % ((widgets * 75) + (gizmos * 112)))