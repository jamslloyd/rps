import random

import funcs

def determine_result(player, computer):
    if player == computer:
        return "tie"
    elif x_beats_y[player] == computer:
        return "win"
    else:
        return "loss"

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

mode = input("\nWhat mode would you like? Best of 3, best of 5 or unlimited (u): ").lower()
while mode not in ["3", "5", "unlimited", "u"]:
    mode = input("\nPlease enter 3, 5 or unlimited (u): ").lower()

if mode in ["unlimited", "u"]:
    wins_needed = 0
else:
    wins_needed = int(mode) // 2 + 1
    print(f"\nFirst to {wins_needed} wins!")

while True:
    player_choice = input("\nYour options are: rock (r), paper (p) and scissors (s)"
                          "\nEnter your choice: ").lower()
    while player_choice not in options:
        if player_choice in short_options:
            player_choice = short_options[player_choice]
        else:
            player_choice = input("Please enter rock (r), paper (p) or scissors (s): ").lower()

    computer_choice = random.choice(options)

    result = determine_result(player_choice, computer_choice)

    if result == "win":
        result_sentence = "You win!"
        player_wins += 1
        computer_losses += 1
    elif result == "tie":
        result_sentence = "It's a tie!"
        ties += 1
    else:
        result_sentence = "You lose!"
        computer_wins += 1
        player_losses += 1

    games_played += 1

    player_win_rate = player_wins / games_played * 100

    computer_win_rate = computer_wins / games_played * 100

    print("\n" + result_sentence + "\n")

    print("You chose: " + player_choice + "\nThe computer chose: " + computer_choice)

    print(f"\nPlayer wins = {player_wins}"
          f"\nPlayer win rate = {player_win_rate:.2f}%"
          f"\nPlayer losses = {player_losses}")
    print(f"\nComputer wins = {computer_wins}"
          f"\nComputer win rate = {computer_win_rate:.2f}%"
          f"\nComputer losses = {computer_losses}")

    print(f"\nGames played = {games_played}"
          f"\nTies = {ties}")

    if wins_needed > 0:
        print(f"\nThe score is: {player_wins} : {computer_wins}")

    if wins_needed == 0:
        if input("\nPlay again?\nyes = y no = n\n").lower() == "n":
            break
    elif player_wins == wins_needed or computer_wins == wins_needed:
        break

if player_wins > computer_wins:
    winner_sentence = "The Player wins the match!"
elif player_wins < computer_wins:
    winner_sentence = "The Computer wins the match!"
else:
    winner_sentence = "The Match ends in a tie!"

print(f"\nFinal result:"
      f"\n{winner_sentence}"
      f"\nYour wins = {player_wins}"
      f"\nYour win rate = {player_win_rate:.2f}%"
      f"\nTies = {ties}"
      f"\nYour losses = {player_losses}")