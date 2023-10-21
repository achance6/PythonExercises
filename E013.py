# Prompts user for an amount of cents, calculates amount
# of each coin to represent that using the least amount
# of coins possible without any iteration or conditionals

cents = int(input("Input an amount of cents: "))
toonies = cents // 200
loonies = (cents % 200) // 100
quarters = ((cents % 200) % 100) // 25
dimes = (((cents % 200) % 100) % 25) // 10
nickels = ((((cents % 200) % 100) % 25) % 10) // 5
pennies = (((((cents % 200) % 100) % 25) % 10) % 5) // 1
print("%d toonies, %d loonies, %d quarters, %d dimes, %d nickels, %d pennies" 
      % (toonies, loonies, quarters, dimes, nickels, pennies))