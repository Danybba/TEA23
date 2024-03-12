""" Compund interest calculator
Wir nutzen unsere Kenntnisse der while Schleifen um zu sehen wie sich der Betrag auf unserem Bankkonto mit einer gegebenen Zinsrate über die Zeit vergrößert.
Wir beginnen damit den Anfangsbetrag, die Zinsrate, und die Jahre der Verzinsung beim Nutzer abzufragen. Diese Daten sollen auch wieder vor der 
Berechnung initial ausgegeben werden. 
Anschließend berechnen und erhöhen wir das Konto um die entsprechend aufgelaufenen Zinsen pro Jahr und geben die Beträge jedes Jahres aus. 
"""

####    Compound interest calculator        ####
####    date: 03.02.2022                    ####
####    author: DS                          ####
####    brief: calculates compund interest  ####

account = float(input("Bitte geben Sie den Anfangsbetrag ein: "))
interest_rate = float(input("Bitte geben Sie die Zinsrate ein: "))
years = float(input("Bitte geben Sie den Zeitraum der Verzinnsung in Jahren ein: "))

print(f"Anfangsbetrag: {account}")
print(f"Zinsrate: {interest_rate}")
print(f"Jahre: {years}")

counter = 1

while counter <= years:
    accrued_interest = account * interest_rate
    account += accrued_interest
    print(f"Jahr {counter}: {account}")
    counter += 1


    
