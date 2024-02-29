""" Ausreißer finden / Finding outliers
- Als erstes benötigen wir ein upper_limit und ein lower_limit um Ausreißer zu 
  identifizieren. Erstellen sie die Variablen und weisen Sie ihnen einen Zahlenwert zu.
- Wir benötigen eine boolsche Variable outlier um das Zwischenergebnis abzuspeichern, 
  welche mit False initialisiert wird. Erstellen und initialisieren Sie diese. 
- Jetzt benötigen wir noch die Zahl die wir prüfen möchten. 
  Diese Fragen wir über die input Funktion vom Nutzer ab und speichern 
  diese in der Variable number. 
- Lassen Sie uns nun prüfen ob number innerhalb des upper_limit liegt. 
  Erstellen Sie hierzu die if Anweisung. 
- Sollte die Zahl größer als upper_limit sein ändern wir den Zustand der 
  Variable outlier zu True. 
- Wir müssen ebenfalls prüfen ob number kleiner als lower_limit ist. 
  Prüfen Sie dies wieder über eine if Anweisung und ändern Sie entsprechend den 
  Status der Variable outlier. 
- Zum Schluss wollen wir über eine if Anweisung prüfen ob outlier True ist.
  Sollte dies der Fall sein geben wir „number is an outlier“ auf der Console aus. 
  Der String soll hierbei den Inhalt der Variable number lesbar ausgeben. """

####    Finding outliers                        ####
####    date: 31.01.2024                        ####
####    author: DS                              ####
####    brief: check if input is an outlier     ####

# CONSTANTS
UPPER_LIMIT = 91
LOWER_LIMIT = 24

# USER INPUT
number = int(input("Enter a Number! "))

# PROGRAMM
result = (number > UPPER_LIMIT) or (number < LOWER_LIMIT)

if result:
    # USER OUTPUT
    print(f"{number} is an outlier")

input()