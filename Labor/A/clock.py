hour = int(input('What time is it? '))

if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
elif hour < 21:
    print("Good evening")
else:
    print("Good night")