""" Heart Rate Data
- Erstelle eine heart_rate Variable, welche die Herzfrequenz des Sensors 
  speichern soll
- Weiße dieser Variable heart_rate einen Zahlenwert 77 zu, 
  sodass wir diesen später mit anderen Zahlen vergleichen können
- Erstelle eine too_low Variable, welche uns sagen wird ob die Frewuenz zu niedrig ist.
- Jetzt prüfe ob die heart_rate kleiner als 60 ist und speichere das Ergebnis in too_low.
- Erstelle eine Variable too_high, welche uns sagen wird ob die Herzfrequenz zu hoch ist. 
- Jetzt prüfe ob die heart_rate größer als 100 ist und speichere das Ergebnis in too_high. 
- Wir möchten dem Nutzer ausgeben ob seine Herzfrequenz zu niedrig ist.
- Dafür starten wir mit der Ausgabe des Textes "Heart rate low:" in der Console
- Jetzt geben wir den Wert too_low in der Console aus
- Ebenfalls möchten wir dem Nutzer ausgeben ob seine Herzfrequenz zu hoch ist. 
- Dafür starten wir mit der Ausgabe des Textes "Heart rate high:" in der Console
- Jetzt geben wir den Wert too_high in der Console aus. 
"""
####    Heart rate                          ####
####    date: 01.02.2024                    ####
####    author: DS                          ####
####    brief: Analize heart frequency      ####

LOWER_RATE = 60
UPPER_RATE = 100

# UISER INPUT

heart_rate = int(input("Enter heart rate, to check if it is too high or to low:"))

# PROGRAMM
too_low = heart_rate < LOWER_RATE
too_high = heart_rate > UPPER_RATE

# USER OUTPUT
print(f"Heart rate low: {too_low}")
print(f"Heart rate high: {too_high}")

input() # to keep the wiondow open

