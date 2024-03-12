##################################################
##                                              ##
## Taschenrechner / Calculator                  ##
##                                              ##
##################################################

# author: 31.01.2022 Daniel Schäftner
# brief: Calculator with 4 basic operations

##################################################
# Usermenue input                                #
##################################################

number_1 = int(input("1. Zahl: "))
number_2 = int(input("2. Zahl: "))
operation = input("Addieren? (+), Subtrahieren? (-), Multiplizieren? (*), Dividieren? (/): ")

#################################################
# Calculation                                   #
#################################################

def calculator (number_1, number_2, operation):

    result = 0
    error = False

    # Add
    if operation == '+':
        result = number_1 + number_2

    # Sub
    elif operation == '-':
        result = number_1 - number_2

    # Mult
    elif operation == '*':
        result = number_1 * number_2

    # Div
    elif operation == '/':
        result = number_1 / number_2

    # wrong operation
    else:
        error = True

    #################################################
    # Result output                                 #
    #################################################

    if not error:
        print(f"Das Ergebnis ist: {result}")
    else:
        print("Rechenoperation nicht unterstützt!")









































calculator(number_1, number_2, operation)
