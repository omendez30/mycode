#/usr/bin/env python 3

import random

answer = input("Would you like to play a game y/n? ")

rps = {"rock":1, "paper":2, "scissors":3}

if answer == "y":
    choice = input("Choose rock, paper, or scissors: ")
    our_choice = random.choice(["rock", "paper", "scissors"])
    print(choice, our_choice)
else:
    exit()

if choice == "rock" and our_choice == "paper":
    print("Paper beats rock, we win!")
elif choice == "paper" and our_choice == "scissors":
    print("Scissor beats paper, we win!")
elif choice == "scissors" and our_choice == "rock":
    print("rock beats scissors, we win!")
elif choice == "paper" and our_choice == "rock":
    print("Paper beats rock, we lose :(")
elif choice == "scissors" and our_choice == "paper":
    print("Scissors beats paper, we lose :(")
elif choice == "rock" and our_choice == "scissors":
    print("rock beats scissors, we lose :(")
else:
    print(f"Same choice selected, draw")



