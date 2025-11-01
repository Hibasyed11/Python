import random
playing=True
number=str(random.randint(0,10))
print("I'm thinking of a number between 0 and 10")
while playing:
    guess=str(input("What's your guess? "))
    if number==guess:
        print("You're right, my number was", number)
        break
    else:
        print("That's not the right number.")