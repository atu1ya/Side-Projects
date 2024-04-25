import random

def numguesser():
    """
    This is a simple number guessing game. The user has to guess a random number between 1 and 20. The user has 3 chances to guess the number, and the game ends when the user guesses the correct number or runs out of chances.
    """
    print("Welcome to Atulya's Number Guesser Game!")
    print("I am thinking of a number between 1 and 20. You have 3 chances to guess the number.")

    number = random.randint(1, 20)  # Random number to be guessed
    chances = 3  # Number of chances to guess the number

    while chances > 0:
        print(f"You have {chances} chances left.")

        # Handle invalid input gracefully
        try:
            guess = int(input("Enter your guess: "))  # Get user input as an integer
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Prompt user again if input is invalid

        if guess == number:
            # If the user guesses correctly
            print("Congratulations! You have guessed the correct number!")
            break

        # Check the difference between the guess and the correct number
        difference = abs(guess - number)

        if difference > 7:
            print("You're very cold! Try again.")
        elif 5 < difference <= 7:
            print("You're getting warmer. Try again.")
        elif 2 < difference <= 5:
            print("You're getting hot. Try again.")
        else:
            print("You're very hot. Try again.")

        chances -= 1  # Decrement the chances after each guess6

    if chances == 0:
        # If the user runs out of chances
        print(f"Sorry! You have run out of chances. The number I was thinking of was {number}. Better luck next time!")

# Run the game
numguesser()
