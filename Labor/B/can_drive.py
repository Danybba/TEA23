age = int(input("What is your age?"))
has_license = input("Has license? y/n")
is_insured = input("Has insurance? y/n")
pre_license = input("Has pre license? y/n")

limit_age = ((age >= 18) and (has_license == "y")) or \
            ((age >= 17) and (pre_license == 'y')) and \
            (is_insured == "y")

if limit_age:
    can_drive = True
else:
    can_drive = False
    
print(can_drive)