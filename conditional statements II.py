grade=int(input("What was raw score"))
if 82 >= grade >= 68:
    print("You achieved mastery on the regents")
elif 68 > grade >= 48:
    print("You got a 4 as you performace level on the regents")
elif 48 > grade >= 29:
    print("You got a 3 as you performace level on the regents")
else: 
    print("You failed the regents")