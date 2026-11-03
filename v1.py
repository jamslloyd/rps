import random

options = ["rock", "paper", "scissors"]

x_beats_y = {"rock": "scissors",
            "paper": "rock",
            "scissors": "paper"}

outcomes = ["win", "tie", "loss"]

result = "nothing"

result_sentence = "nothing"

print("\nWelcome to rock paper scissors!")

while True:
    player_choice = input("\nYour options are: rock, paper and scissors"
                          "\nEnter your choice: ").lower()
    while player_choice not in options:
        player_choice = input("Please enter rock, paper or scissors: ").lower()

    computer_choice = random.choice(options)

    if player_choice == computer_choice:
        result = "tie"
    elif x_beats_y[player_choice] == computer_choice:
        result = "win"
    else:
        result = "loss"

    if result == "win":
        result_sentence = "You win!"
    elif result == "tie":
        result_sentence = "It's a tie!"
    elif result == "loss":
        result_sentence = "You lose!"

    print("\n" + result_sentence + "\n")

    print("You chose: " + player_choice + "\nThe computer chose: " + computer_choice)

    if input("\nPlay again?\nyes = y no = n\n").lower() == "n":
        break