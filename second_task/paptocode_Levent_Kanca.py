import random
age=0 
license=()
drunk=()
test=False
parents= False
counter=0
number1=0
number2=0
answer=0
result=0
fahren=False


age= int(input("Wie Alt bist du?"))
if age>17:
    license = input("Besitzt du einen Führerschein? (y/n)")
    if license =="y":
        drunk= input("Hast du Alkohol getrunken? (y/n)")
    else:
        parents=True
    if drunk=="y":
        while counter<3:
            number1=random.randint(1,100)
            number2=random.randint(1,100)
            result= number1 + number2
            print("Was ergibt " + str(number1) + " + " + str(number2) + "?\n")             
            answer=int(input())
            if answer==result:
                counter += 1
            else:
                parents= True
                counter =+3
        if parents== False:
            fahren=True
    else:
        fahren=True
        
else:
    parents=True

if parents== True:
    print("Bitte rufe deine Eltern an.")

if fahren==True:
    print("Ok, du kannst nach Hause fahren.")
