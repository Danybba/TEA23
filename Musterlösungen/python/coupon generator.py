""" Coupon generator
- Wir verwenden eine for Schleife um das Erstellen mehrerer Gutscheine für eine 
  Webseite zu vereinfachen. 
- Wir bauen mehrere Teile eines Links zusammen um die Gutschiene zu generieren.
- Wir erstellen eine Variable base die den Name der Webseite für die wir die Coupons 
  erstellen, beinhaltet. z.B. www.netflix.com
- Weiter noch eine Variable coupon die die Art des Gutschiens spezifiziert. 
  z.B. signup/coupon
- Als nächsten Schritt wollen wir über die Eingabefunktion abfragen wieviel 
  Prozent discount wir geben möchten.  
- Schlussendlich wollen wir noch die Anzahl der zu erstellenden Gutscheine 
  eingeben können. 
- Die for Schliefen baut uns die einzelnen Teile zusammen. Wir bauen die for 
  Schleife mit num und range() auf. 
- Wir möchten Gutschiene von 0 beginnen bis zur eingegebenen Anzahl erstellen.
- Wir möchten die Gutschein Links zusammengesetzt ausgeben. Verwenden Sie hierzu 
  einen f string der sich wie folgt zusammenbaut. base/coupon/discount/num.
- Ein weiteres print statement soll uns zum Schluss anzeigen wie viele Gutscheine 
  erstellt wurden. 
"""


####    Coupon generator                        ####
####    date: 14.02.2022                        ####
####    author: DS                              ####
####    brief: generate coupons for netflix     ####

base = "www.netflix.com"
coupon = "signup/coupon"
discount = int(input("Discount:"))
amount = int(input("Anzahl:"))

for num in range(amount):
    print(f"{base}/{coupon}/{discount}/{num}")

print(f"{amount} coupons created")

