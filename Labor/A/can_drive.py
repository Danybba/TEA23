age = int(input("What is your age?"))
pre_license = input("Has pre license? y/n")
has_license = input("Has license? y/n")
is_insured = input("Has insurance? y/n")



if (age >= 18) and ((pre_license == 'y') or ("y" in has_license)) and (is_insured == "y"):
    can_drive = True
else:
    can_drive = False

print(can_drive)

input()

