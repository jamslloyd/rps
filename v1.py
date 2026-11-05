import random

options = ["rock", "paper", "scissors"]

short_options = {"r" : "rock", "p" : "paper", "s" : "scissors"}

x_beats_y = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

computer_wins = 0
computer_losses = 0

games_played = 0

ties = 0

player_wins = 0
player_losses = 0

print("\nWelcome to rock paper scissors!")

while True:
    player_choice = input("\nYour options are: rock (r), paper (p) and scissors (s)"
                          "\nEnter your choice: ").lower()
    while player_choice not in options:
        if player_choice in short_options:
            player_choice = short_options[player_choice]
        else:
            player_choice = input("Please enter rock (r), paper (p) or scissors (s): ").lower()

    computer_choice = random.choice(options)

    if player_choice == computer_choice:
        result = "tie"
        ties +=1
    elif x_beats_y[player_choice] == computer_choice:
        result = "win"
        player_wins += 1
        computer_losses += 1
    else:
        result = "loss"
        computer_wins += 1
        player_losses += 1

    games_played += 1

    player_win_chance = player_wins/games_played*100

    computer_win_chance = computer_wins/games_played*100

    if result == "win":
        result_sentence = "You win!"
    elif result == "tie":
        result_sentence = "It's a tie!"
    else:
        result_sentence = "You lose!"

    print("\n" + result_sentence + "\n")

    print("You chose: " + player_choice + "\nThe computer chose: " + computer_choice)

    print(f"\nPlayer wins = {player_wins}"
          f"\nPlayer losses = {player_losses}"
          f"\nPlayer win chance = {player_win_chance:.2f} %")
    print(f"\nComputer wins = {computer_wins}"
          f"\nComputer losses = {computer_losses}"
          f"\nComputer win chance = {computer_win_chance:.2f} %")

    print(f"\nGames played = {games_played}"
          f"\nTies = {ties}")

    if input("\nPlay again?\nyes = y no = n\n").lower() == "n":
        break