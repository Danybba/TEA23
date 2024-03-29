##################################################
##                                              ##
## Taschenrechner / Calculator                  ##
##                                              ##
##################################################

# author: 31.01.2022 Daniel Schäftner
# brief: Calculator with 4 basic operations

#################################################
# Calculation                                   #
#################################################

def add (number_1, number_2):
    return number_1 + number_2

def sub (number_1, number_2):
    return number_1 - number_2

def mul (number_1, number_2):
    return number_1 * number_2

def div (number_1, number_2):
    return number_1 / number_2

def calculator (number_1, number_2, operation):

    result = 0
    error = False

    # Add
    if operation == '+':
        result = add(number_1,number_2)

    # Sub
    elif operation == '-':
        result = sub(number_1,number_2)

    # Mult
    elif operation == '*':
        result = mul(number_1,number_2)

    # Div
    elif operation == '/':
        result = div(number_1,number_2)

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

