##################################################
##                                              ##
## pap to code driver license and alc           ##
##                                              ##
##################################################

# author: 03.03.2023 Daniel Schäftner
# brief: Pap to Code example

##################################################
# import libs                                    #
##################################################
import random

##################################################
# functions                                      #
##################################################
def alc_test():
    loop = True

    while(loop):
        num1 = random.randrange(9)
        num2 = random.randrange(9)
        print(f"Bitte addiere {num1} mit {num2}!")
        result = int(input())

        if(result == (num1 + num2)):
            loop = False
            return 1

#################################################
# process                                       #
#################################################

test_passed = False
test_count = 0

age = int(input("Wie alt bist du?:"))
if (age >= 18):
    driver_license = input("Hast du einen Führerschein? (Y/N):")
    if(driver_license == "Y"):
        alcohol = input("Hast du Alkohol getrunken? (Y/N):")
        if(alcohol == "N"):
            test_passed = True
        else:
            for i in range(3):
                test_count += alc_test()

            if(test_count == 3):
                test_passed = True

#################################################
# result output                                 #
#################################################

if test_passed:
    print("Ok, du kannst nach Hause fahren!")
else:
    print("Bitte ruf deine Eltern an!")