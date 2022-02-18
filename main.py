import random

#introduction
print("Let's play a game of rock, paper scissors! There will be 3 rounds. Best score wins!")

#variables
player_score = 0
computer_score = 0
computer_choice = random.randrange(1, 3)
round_number = 1

#loops through 3 rounds
while round_number < 4:
    print(f"ROUND {round_number}")
    print("Choose 1 for rock, 2 for paper, or 3 for scissors.")
    player_choice = int(input())
    if player_choice not in range(1, 4):
        print("Try again. Selection must be 1, 2, or 3.")
        player_choice = int(input())
    print(f"You chose: {player_choice}!")
    print(f"The computer chose: {computer_choice}")
    if player_choice == 1 and computer_choice == 1:
        print("It's a tie! No points will be added to either score.")
    elif player_choice == 1 and computer_choice == 2:
        print("Paper covers rock. The computer wins.")
        computer_score += 1
    elif player_choice == 1 and computer_choice == 3:
        print("Rock smashes scissors. You win this round!")
        player_score += 1
    elif player_choice == 2 and computer_choice == 1:
        print("Paper covers rock. You win!")
        player_score += 1
    elif player_choice == 2 and computer_choice == 2:
        print("It's a tie! No points will be added to either score.")
    elif player_choice == 2 and computer_choice == 3:
        print("Scissors cut paper! The computer wins this round!")
        computer_score += 1
    elif player_choice == 3 and computer_choice == 1:
        print("Rock smashes scissors. This round goes to the computer.")
        computer_score += 1
    elif player_choice == 3 and computer_choice == 2:
        print("Scissors cut paper. You win!")
        player_score += 1
    elif player_choice == 3 and computer_choice == 3:
        print("It's a tie. No points will be added to either score.")
    round_number += 1

#declares the winner
print(f"You scored {player_score} points. The computer scored {computer_score} points.")
if player_score > computer_score:
    print("You win!")
elif player_score == computer_score:
    print("It's a tie!")
else:
    print("The computer won!")
