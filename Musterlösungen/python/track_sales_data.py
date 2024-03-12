####    track_sales_data                        ####
####    date: 27.01.2022                        ####
####    author: DS                              ####
####    brief: track the sales data of jeans    ####

jeans_stock = 600
jeans_sold = 501
sale_target = 500

target_hit = jeans_sold == sale_target
print("Hit jenas sale target: ")
print(target_hit)

current_stock = jeans_stock - jeans_sold
in_stock = current_stock != 0
print("Jeans in stock:")
print(in_stock)