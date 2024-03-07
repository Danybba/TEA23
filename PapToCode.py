age = int(input("Wie alt bist du?"))

def drive_home():
    print("Ok, du kannst nach Hause fahren!")

def alcohol_test():
    correct_ans = 0
    for i in range(3):
        result = int(input("1 + 2 = "))

        if result == 1 + 2:
            correct_ans += 1

    return correct_ans

if age >= 18:
 
    driver_license = input("Hast du einen Führerschein (Y/N)?")
    if driver_license == "Y":

        drunk = input("Hast du Alkohol getrunken? (Y/N)")
        if drunk == "Y":
            
            if alcohol_test() == 3:
                drive_home()
            else:
                print("Bitte ruf eine Eltern an!")
        else:
            drive_home()
    
    else:
        print("Bitte ruf eine Eltern an!")
else:
    print("Bitte ruf eine Eltern an!")

    