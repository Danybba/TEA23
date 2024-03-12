""" User database
Lasst uns Bedingungen nutzen um zu prüfen ob ein Nutzer zur Datenbank hinzugefügt wurde oder nicht. 
Erstelle eine Variable user_added und weise einen boolschen Wert zu. 
Erstelle eine Variable user und weise einen Namen (string) zu. 
Frage ab ob user_added gleich False ist. Wenn ja, gebe den string „Adding user to dartabase“ aus. 
Die Variable user soll hier im String verwendet werden.
Setzen im Code Block der Bedingung user_added auf True.
Anschließend gebe außerhalb der Bedingung aus „Database has user: user“ Die Variable user soll hier 
im String verwendet werden.
"""

####    User database                       ####
####    date: 31.01.2022                    ####
####    author: DS                          ####
####    brief: add user to database         ####

user_added = True
user = "Becca"

if user_added == False:
    print(f"Adding {user} to database")
    user_added = True
print(f"Database has user: {user}")


