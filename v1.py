import random

outcome_sentence = "nothing"

print("\nWelcome to rock paper scissors!")

while True:
    player_choice = input("\nYour options are: rock, paper and scissors"
                          "\nEnter your choice: ").lower()
    while player_choice not in ["rock", "paper", "scissors"]:
        player_choice = input("Please enter rock, paper or scissors: ").lower()

    computer_choice = random.choice(["win", "tie", "lose"])

    outcome = computer_choice

    if outcome == "win":
        outcome_sentence = "You win!"
    elif outcome == "tie":
        outcome_sentence = "It's a tie!"
    elif outcome == "lose":
        outcome_sentence = "You lose!"

    print("\n" + outcome_sentence + "\n")

    if input("Play again?\nyes = y no = n\n").lower() == "n":
        break