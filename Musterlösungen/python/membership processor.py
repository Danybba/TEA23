""" Mitgliedschaft Verwaltung / membership processor
- Ein Club hat eine Mitgliedschaft Anmeldung von wo aus alle Daten bei 
  uns als strings ankommen.
  Es kann angenommen werden das folgende Werte ankommen. (Gegeben) 

name_box = "John Schnee"
age_box = "20"
uni_box = "" 
subs_box = "1.99"
mkt_box = "0"

- Verwendet mit strings gibt die bool() Funktion True zurück wenn ein string nicht 
  leer ist, andernfalls False. 
  Prüfen Sie name_box auf Inhalt ab. Wenn ein Inhalt vorhanden ist wird dieser 
  in eine Variable name gespeichert. Falls kein Inhalt vorhanden ist wird der string 
  Unknown in die Variable name gespeichert.

- Generiere aus dem Wert von age_box eine integer und weise ihn der Variable age zu. 
  Setze den Wert der Variable student auf True wenn uni_box einen Wert beinhaltet. 
  subs_box soll so konvertiert werden, das die Dezimalstellen nicht verloren gehen wenn 
  wir den Wert in subscription speichern. 
  mkt_box beinhaltet den String Wert 0 oder 1. Verwende Konvertierungen um diese Werte 
  entsprechend in True oder False umzuwandeln und in marketing zu speichern.

- Schlussendlich erstelle eine Profile Zeile für die Mitglieder Seite, die den name 
  und die Werte in age, student, subscription und marketing als Teil eines strings 
  verwendet. Der string soll sich wie folgt zusammensetzten und ausgegeben werden. 
  name, age, student, subscription, marketing
"""

####    Membership processor                    ####
####    date: 31.01.2022                        ####
####    author: DS                              ####
####    brief: convert the string               ####

name_box = "John Schnee"
age_box = "20"
uni_box = ""
subs_box = "1.99"
mkt_box = "0"

name_entered = bool(name_box)
if name_entered:
    name = name_box
else:
    name = "Unknown"

age = int(age_box)
student = bool(uni_box)
subscription = float(subs_box)
marketing = bool(int(mkt_box))

profile = (name + ', ' 
                + str(age) + ', ' 
                + str(student) + ', \n' 
                + str(subscription) + ', ' 
                + str(marketing))
print(profile)





