# print("hello world")
# print("my name is: Daniel")
# print("3")
# print("2")
# print("1")
# print("GO")

# city = "Miami"
# # city = 12 # Kommentar
# city_2 = "Köln"

# # city = city_2

# percent = 3 / 100
# print(percent)

# print("Followers:" + "55")
# print(city + city_2)

# private = "3"
# puplic = "10"

# total = private + puplic
# print("Total posts: ")
# print(total)

# powered_on = True
# print(not powered_on)

# pin = 5
# print(pin != 6)

# print(1 >= 1)

# print("online" != "offline")


# pin = 5
# print(type(pin))
# pin = "5"
# print(type(pin))
# pin = True
# print(type(pin))
# pin = 5.13
# print(type(pin))

# # pin = input()
# print(type(pin))
# # pin = int(input())
# print(type(pin))

# new_messages = 5
# read_messages = 2
# print(f" {new_messages - read_messages} new messages")

# help(input)

# answer = input("Wer war ein berühmter Maler?")

# if answer == "Picasso":
#     print(answer + " is correct!")

# if answer != "Picasso":
#     print(answer + " is wrong!") 

# age = int(input("What is your age?"))

# limit_age = age >= 18

# if not limit_age:
#     print("too young!")

# var = 9

# if True or (var == 10):
    
# def greet_user(name):
#     print(name)
#     print("Welcome back")
#     print("!!!")


# greet_user("Anna")
# greet_user("Emil")

# greet_user("xxxxxxxxxxxxxxxxxxxxxxxxxxx")

import pygal

pie = pygal.Pie()

pie.title = "Time spend on social network"
pie.add("Twitter", 47)
pie.add("Facebook", 23)
pie.add("Instagram", 30)

pie.render_in_browser()