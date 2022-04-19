#!/usr/bin/env python3

round = 0
answer = ""

while round < 3 and (answer != "Brian" and != "Shruberry"):
    round += 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______"').capitalize()
    

    if answer == "Brian":
        print("Correct")
        break
    elif answer == "Shruberry":
        print("You gave the super scret answer!")
        break
    elif round==3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")


