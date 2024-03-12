# Wir wollen die Herzfrequenz eines Patienten analysieren. 
# Wir verwenden Vergleiche um zu prüfen ob die Herzfrequenz zu niedrig oder zu hoch ist.
# Wir möchten das Ergebnis ausgeben. 

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
####    date: 27.01.2022                    ####
####    author: DS                          ####
####    brief: Analize heart frequency      ####


heart_rate = 77

too_low = heart_rate < 60
too_high = heart_rate > 100

print("Heart rate low:")
print(too_low)

print("Heart rate high:")
print(too_high)