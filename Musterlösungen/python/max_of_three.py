####    Max of three                            ####
####    date: 03.02.2022                        ####
####    author: DS                              ####
####    brief: find the max of three numbers    ####

def max_of_two( x, y ):
    if x > y:
        return x
    else:
        return y

def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )

def user_inputs():
    global num_1
    num_1 = int(input("Zahl 1:"))
    global num_2
    num_2 = int(input("Zahl 2:"))
    global num_3
    num_3 = int(input("Zahl 3:"))

def outputs():
    print(max_of_three(num_1, num_2, num_3))


#Loop
while(True):
   user_inputs()
   outputs()


