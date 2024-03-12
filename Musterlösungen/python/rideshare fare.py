""" Fahrpreis Mitfahrgelegenheit / Rideshare fare
- Wir verwenden unsere Kenntnisse zu if, elif und else Bedingungen um einen Fahrpreis 
  der Mitfahrgelegenheit abhängig von der Fahrtenart zu kalkulieren. 
  Erstellen Sie die Variablen ride_type. Fragen Sie über die input Funktion vom 
  Nutzer ab ob er ein Fahrtenupgrade plus oder comfort haben möchte. Wir möchten hier 
  den String speichern. 
- Weiter fragen wir den Nutzer ab ob er verfügbare Credits hat. Dieser soll uns die 
  Anzahl seiner credits eingeben, welche wir in einer Variable credits speichern.  
  Wir erstellen eine Variable ride_price und final_price und initialisieren diese 
  mit dem Wert 0. 
- Jetzt prüfen wir ab ob ride_type dem String plus entspricht. Sollte dies der Fall 
  sein, aktualisieren wir ride_price auf 20,5. Sollte dies nicht der Fall sein, 
  prüfen wir ride_type auf comfort ab. Ist das der Fall aktualisieren wir ride_price 
  auf 37,9. Trifft keine der beiden Abfragen zu so wir der Preis ride_price auf 
  18,7 festgelegt.
- Nun geben wir den Fahrpreis auf der Console kommentiert aus. Der String soll hierbei 
  den Inhalt der Variable ride_price beinhalten. Immer wenn die Anzahl der vom Nutzer 
  eingegebenen Credits größer 0 ist, möchten wir eine Verrechnung dieser durchführen, 
  wobei die credits vom ride_price abgezogen und in final_price gespeichert werden. 
- Nun geben wir den finalen Fahrpreis ebenfalls auf der Console kommentiert aus. 
  Der String soll hierbei den Inhalt der Variable final_price beinhalten. 
"""

####    Rideshare fare                          ####
####    date: 31.01.2022                        ####
####    author: DS                              ####
####    brief: calculating ride price           ####

ride_type = input("Wählen Sie bei Bedarf eine Farten upgrade aus: plus oder comfort!")
credits = int(input("Geben Sie die Anzahl ihrer verfügbare Credits ein!"))

ride_price = 0
final_price = 0

if ride_type == "plus":
    ride_price = 20.5
elif ride_type == "comfort":
    ride_price = 37.9
else:
    ride_price = 18.7

print("Fahrpreis:", ride_price)

if credits > 0:
    final_price = ride_price - credits
    print("Finaler Preis nach Abzug der Credits:", final_price)





