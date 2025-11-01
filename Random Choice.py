import random
while True:
    possible_actions=["Rock", "Paper", "Scissors"]
    computer_choice=(random.choice(possible_actions))
    your_choice=input("What is your choice ")
    print(f"You chose {your_choice}, and the computer chose {computer_choice}")
    if your_choice == computer_choice:
        print("It's a tie!!!")
    elif your_choice=="Scissors":
        if computer_choice=="Paper":
            print("Scissor cut paper, You Win!")
        else:
            print("Rock smashes scissors, You Lose")
    elif your_choice=="Paper":
        if computer_choice=="Scissore":
            print("Scissor cut paper, You Lose")
        else:
            print("Paper covers rock, You Win!")
    elif your_choice=="Rock":
        if computer_choice=="Paper":
            print("Paper covers rock, You Lose")
        else:
            print("Rock smashes scissors, You Win!")
    play_again=input("Do you want to play again? y or n ")
    if play_again=="n":
        break