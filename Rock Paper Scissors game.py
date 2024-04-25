# Rock Paper Scissors game

import random

def rockpaperscissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors")
    user_choice = input()
    user_choice = user_choice.lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose {computer_choice}")
    if computer_choice == user_choice:
        print("It's a tie!")
        
    elif computer_choice == "rock" and user_choice == "scissors":
        print("Computer wins!")
    elif computer_choice == "rock" and user_choice == "paper":
        print("You win!")
    elif computer_choice == "paper" and user_choice == "rock":
        print("Computer wins!")
    elif computer_choice == "paper" and user_choice == "scissors":
        print("You win!")
    elif computer_choice == "scissors" and user_choice == "rock":
        print("You win!")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("Computer wins!")
    else:
        print("Invalid choice. Please choose between rock, paper or scissors.")
    
    print("Do you want to play again? (yes or no)")
    play_again = input()
    if play_again.lower() == "yes":
        rockpaperscissors()
    else:
        print("Thanks for playing!")


rockpaperscissors()