import random
import time
number=random.randint(1,100)
def intro():
    global Name
    Name=input("What is your name? ")
    print("Hi {0}, I'm going to pick a random  numbder between 1 and 100, and you have to guess it!".format(Name))
    if (number%2==0):
        x='even'
    else:
        x='odd'
    print("\nThis is an {} number".format(x))
    time.sleep(.5)
    print("Go ahead. Guess!")
def pick():
    global Name
    guessesTaken = 0
    while guessesTaken < 6:
        enter = input("Guess: ")
        try:
            guess = int(enter)
            guessesTaken += 1
            if guess < number:
                print("Higher")
                print("Try Again!")
            elif guess > number:
                print("Lower")
                print("Try Again!")
            else:
                print("You got it correct!!!")
                print("Good Job {0}! You guessed the number in {1} guesses!".format(Name, guessesTaken))
                break
        except:
            print(enter + " is not a number.")
    if guessesTaken == 6 and guess != number:
        print("Nope, the number I was thinking of is", number)
playagain="yes"
while playagain=="Yes" or playagain=="yes" or playagain=="y" or playagain=="Y":
    intro()
    pick()
    playagain=input("Do you want to play again? ")