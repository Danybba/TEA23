""" Survey data
Wir prüfen die Nutzerantworten einer Umfrage aus einer Fitness App 
im Bezug auf Haufigkeit (frequency)
und intesität (intensity) und geben die Ergebnisse aus. 
Der aktuelle Nutzer macht einmal in der Woche Sport. Erstelle eine Variable 
frequency und weise den Wert "once a week" zu
Als nächstes Speichere die Antwort des Nutzers zur Intensität in der Variable 
intensity und weise den Wert "low" zu. 
Um einen Nutzer als highly_active zu markieren, müssen wir prüfen ob seine frequency 
dem Wert "daily" entspricht und abspeichern.
Als nächstes zeigen wir Highly active user: in der Console an. 
Zuletzt geben wir den Wert von highly_active in der Console aus.
Um einen Nutzer als high_intensity zu markieren, müssen wir prüfen ob seine 
Intensität dem Wert "high" entspricht und abspeichern.
Als nächstes Zeigen wir High intensity sports: in der Console an. 
Zuletzt geben wir den Wert von high_intensity in der Console aus. 
"""

####    Survey data                         ####
####    date: 27.01.2022                    ####
####    author: DS                          ####
####    brief: check survey data            ####

frequency = "once a week"
intensity = "low"

highly_active = frequency == "daily"
print("Highly active user:")
print(highly_active)

high_intensity = intensity == "high"
print("High intensity sports:")
print(high_intensity)
