import sys



alter = int(input("Wie alt bist du?    "))

if alter >=18:
    führerschein= input("Hast du einen Führerschein? Y = Ja / N = Nein    ")
    if führerschein == 'N':
        print("Rufe bitte deine eltern an!")
        sys.exit()
else:
    print("Rufe bitte deine eltern an!")
    sys.exit()
   
    
alkohol= input("Hast du Alkohol getrunken? Y = Ja / N = Nein    ")

if alkohol == 'N':
    print("Fahre bitte nach Hause")
    sys.exit()
   
if alkohol == 'Y':
    n = 0
    while True:
        ergebnis = int(input("Was ist 2 + 3 = ? "))
        if ergebnis == 5:
            print("Fahren Sie bitte nach Hause.")
            sys.exit()
        else:
            print("Falsche Antwort. Bitte versuchen Sie es erneut.")
            n += 1
            if n >= 3:
                print("Sie haben drei Mal falsch geraten. Bitte übergeben Sie Ihre Schlüssel und rufen Sie ein Taxi an.")
                sys.exit()
        
    
        
   



