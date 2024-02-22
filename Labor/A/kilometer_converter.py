''' This programm calculates miles into kilometers '''
# Author: Daniel
# Date: 2024 

### CONSTANTS
FACTOR = 1.609344 # factor to calculate kilometers from miles
PI = 3.14

### VARIABLES
# miles = 500

### PROGRAMM

miles = int(input("Please enter miles value: "))

kilometers = miles * FACTOR

print("This is the calculated kilometer value:")
print(kilometers)
input("Press Enter to close the programm!")

