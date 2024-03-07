#######################################
#######    author: Jan         ########
#######    date:07.03.2024     ########
#######################################

#defining variables
allowance=False
Zahl1=6
Zahl2=7
Ergebnis=Zahl1+Zahl2

#defining function "Alkoholtest"
def Alkoholtest():
    Test=False
    while Test==False:
        print(f"Was ergibt {Zahl1} + {Zahl2} ?")
        Input=int(input(""))
        if Input==Ergebnis:
            Test=True

#defining function "nachhause"
def nachhause():
    print("Nach Hause fahren")

age=int(input("Wie alt bist du?"))
if age>=18:
    permit=input("Hast du einen Führerschein? (Y/N)")
    if permit=="Y":
        alcohol=input("Hast du Alkohol getrunken? (Y/N)")
        if alcohol=="N":
            allowance=True
        elif alcohol=="Y":
            for i in range(0,3):
                Alkoholtest()
            allowance=True

if allowance==True:
    nachhause()
else:
    print("Bitte ruf deine Eltern an!")