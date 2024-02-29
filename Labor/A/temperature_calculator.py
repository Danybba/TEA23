##################################################
##                                              ##
## Programm zur Umwandlung von Temperaturen     ##
##                                              ##
##################################################

# author: 25.01.2022 Daniel Schäftner
# brief: Umwandlung verschiednen Temperatureinheiten

##################################################
# Nutzermenü                                     #
##################################################

print("(1) Umrechnung von Celsius nach Kelvin")
print("(2) Umrechnung von Celsius nach Fahrenheit")
print("(3) Umrechnung von Kelvin nach Celsius")
print("(4) Umrechnung von Kelvin nach Fahrenheit")
print("(5) Umrechnung von Fahrenheit nach Celsius")
print("(6) Umrechnung von Fahrenheit nach Kelvin")

wahl = input("Bitte wählen: ")

#################################################
# Auswertung der Eingabe und Umrechnung         #
#################################################

# Umrechnung von Celsius nach Kelvin
if wahl == "1": 

    celsius = float(input("Temperatur in Celsius: "))

    if celsius >= -273.15:
        kelvin = celsius + 273.15
        print(f"{celsius}°C = {kelvin}K")
    else:
        print("Fehler: unmögliche Temperatur!")

# Umrechnung von Celsius nach Fahrenheit
elif wahl == "2": 

    celsius = float(input("Temperatur in Celsius: "))

    if celsius >= -273.15:
        fahrenheit = 32.0 + 1.8*celsius             # C * (1/(5/9)) + 32 = F    -> F = 32 + (9/5) * C   -> F = 32 + 1.8 * C
        print(f"{celsius}°C = {fahrenheit}F")   
    else:
        print("Fehler: unmögliche Temperatur!")   

# Umrechnung von Kelvin nach Celsius       
elif wahl == "3":

    kelvin = float(input("Temperatur in Kelvin: "))

    if kelvin >= 0.0:
        celsius = kelvin - 273.15
        print(f"{kelvin}K = {celsius}°C")
    else:
        print("Fehler: unmögliche Temperatur!")  

# Umrechnung von Kelvin nach Fahrenheit            
elif wahl == "4":

    kelvin = float(input("Temperatur in Kelvin: "))

    if kelvin >= 0.0:    
        fahrenheit = kelvin*1.8 - 459.67             # F = 32 + 1.8 * C     -> F = 32 + 1.8 * (K - 273.15)      -> F = 32 + 1.8*K - 491.67      -> F = K * 1.8 - 459.67
        print(f"{kelvin}K = {fahrenheit}F")
    else:
        print("Fehler: unmögliche Temperatur!")    

# Umrechnung von Fahrenheit nach Celsius           
elif wahl == "5":

    fahrenheit = float(input("Temperatur in Fahrenheit: ")) 

    if fahrenheit >= -459.67: # = 0K
        celsius = 5.0*(fahrenheit - 32.0)/9.0
        print(f"{fahrenheit}F = {celsius}°C") 
    else:
        print("Fehler: unmögliche Temperatur!")     

# Umrechnung von Fahrenheit nach Kelvin           
elif wahl == "6":

    fahrenheit = float(input("Temperatur in Fahrenheit: ")) 

    if fahrenheit >= -459.67: # = 0K    
        kelvin = (fahrenheit + 459.67)/1.8          # F = K * 1.8 - 459.67      -> F + 459.67 = K * 1.8     -> K = (F + 459.67)/1.8
        print(f"{fahrenheit}F = {kelvin}K") 
    else:
        print("Fehler: unmögliche Temperatur!")      

# Falsche Eingabe          
else:
    print("Falsche Eingabe!")





