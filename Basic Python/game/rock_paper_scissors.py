#  basic rock, paper, scissors game;
import random
while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    if(player == computer):
        print("computer's choice ", computer)
        print("player's choice: ", player)
        print("Ooop! it's Tie")
    elif player == "rock":
        if computer == "paper":
            print("compter", computer)
            print("player", player)
            print("You lose!")
        if computer == "scissors":
            print("compter", computer)
            print("player", player)
            print("You Win!")
    elif player == "scissors":
        if computer == "paper":
            print("compter", computer)
            print("player", player)
            print("You Win!")
        if computer == "rock":
            print("compter", computer)
            print("player", player)
            print("You lose!")
    elif player == "paper":
        if computer == "rock":
            print("compter", computer)
            print("player", player)
            print("You Win!")
        if computer == "scissors":
            print("compter", computer)
            print("player", player)
            print("You lose!")

    playe_again = input("playe again? (Yes/No) : ").lower()
    if(playe_again != 'yes'):
        break

print("Bye!")
    