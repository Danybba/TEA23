"""Der Code soll eine Verkaufszahl mit einem Verkaufsziel vergleichen und ausgeben ob dieses erreicht wurde.
Weiterhin soll der Code angeben, wie viele Jeans noch auf Lager sind."""
# variables
jeans_stock = 600

jeans_sold = 400

sales_target = 500

#code
if jeans_sold == sales_target:
    print ("Das Verkaufsziel wurde erreicht.")
else:
    print ("Das Verkaufsziel wurde nicht erreicht.")

jeans_stock_new = jeans_stock - jeans_sold

print ("Der Lagerbestand liegt bei " + str(jeans_stock_new) + ".") 