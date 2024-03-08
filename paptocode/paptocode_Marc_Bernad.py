"""
This program checks if the user is allowed to drive

Author: Marc Bernad
Date: 2024/03/07
"""


#VARIABLES
passed = 0
limit_age = 18 #age at which you are allowed to drive
test_repeats = 3 #how many times the alcohol test is repeated
can_drive = True
test_number1, test_number2 = 14, 21

#ALCOHOL TEST FUNCTION
def alcohol_test():
    result = int(input(f"{test_number1} + {test_number2} = "))
    if result == test_number1 + test_number2:
        return 1
    else:
        return 0

#DRIVE HOME FUNCTION
def drive_home():
    print("Ok, du kannst nach Hause fahren!")

#PROGRAM
age = int(input("Wie alt bist du?\n"))

if age < limit_age:
    license = input("Hast du einen Führerschein? (Y/N)\n")
    if license == "Y":
        alcohol = input("Hast du Alkohol getrunken? (Y/N)\n")
        if alcohol == "Y":
            for i in range(test_repeats):
                passed += alcohol_test()
            if passed != test_repeats:
                can_drive = False
    else:
        can_drive = False
else:
    can_drive = False

#USER OUTPUT
if can_drive == True:
    drive_home()
else:
    print("Bitte ruf deine Eltern an!")