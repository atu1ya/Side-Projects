
import random


def easymode():
    """
    Easy mode means they have to guess a number between 1 and 10. They have 3 chances to guess the number.
    """
    print("You have chosen easy mode. Good luck!")
    print("You have 5 chances to guess the number between 1 and 10.")

    number = random.randint(1, 10)  # Random number to be guessed
    chances = 5  # Number of chances to guess the number

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

        if difference > 6:
            print("You're freezing cold! Try again.")
        elif 6 <= difference < 4:
            print("You're cold! Try again.")
        elif 4 <= difference < 2:
            print("You're warm! Try again.")
        else:
            print("You're hot! Try again.")

        chances -= 1  # Decrement the chances after each guess

    if chances == 0:
        # If the user runs out of chances
        print(f"Sorry! You have run out of chances. The number I was thinking of was {number}. Better luck next time!")

def mediummode():
    """
    This is a simple number guessing game. The user has to guess a random number between 1 and 15. The user has 3 chances to guess the number, and the game ends when the user guesses the correct number or runs out of chances.
    """
    print("You have chosen medium mode. Good luck!")
    print("You have 5 chances to guess the number between 1 and 15.")

    number = random.randint(1, 15)  # Random number to be guessed
    chances = 5  # Number of chances to guess the number

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

        if difference > 6:
            print("You're freezing cold! Try again.")
        elif 6 <= difference < 4:
            print("You're cold! Try again.")
        elif 4 <= difference < 2:
            print("You're warm! Try again.")
        else:
            print("You're hot! Try again.")


        chances -= 1  # Decrement the chances after each guess

    if chances == 0:
        # If the user runs out of chances
        print(f"Sorry! You have run out of chances. The number I was thinking of was {number}. Better luck next time!")

def hardmode():
    """
    This is a simple number guessing game. The user has to guess a random number between 1 and 20. The user has 3 chances to guess the number, and the game ends when the user guesses the correct number or runs out of chances.
    """
    print("You have chosen hard mode. Good luck!")
    print("You have 5 chances to guess the number between 1 and 20.")

    number = random.randint(1, 20)  # Random number to be guessed
    chances = 5  # Number of chances to guess the number

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

        if difference > 6:
            print("You're freezing cold! Try again.")
        elif 6 <= difference < 4:
            print("You're cold! Try again.")
        elif 4 <= difference < 2:
            print("You're warm! Try again.")
        else:
            print("You're hot! Try again.")

        chances -= 1  # Decrement the chances after each guess

    if chances == 0:
        # If the user runs out of chances
        print(f"Sorry! You have run out of chances. The number I was thinking of was {number}. Better luck next time!")


def numguesser():
    """
    This is a simple number guessing game. The user has to guess a random number between 1 and 20. The user has 3 chances to guess the number, and the game ends when the user guesses the correct number or runs out of chances.
    """
    print("Welcome to Atulya's Number Guesser Game!")
    
    print("How hard do you want the game to be? Choose a difficulty level:") # Choose difficulty level
    print("1. Easy (1-10)")
    print("2. Medium (1-15)")
    print("3. Hard (1-20)")
    userinput = int(input("Enter the number corresponding to the difficulty level: "))

    if userinput == 1:
        easymode()
    
    elif userinput == 2:
        mediummode()
    
    elif userinput == 3:
        hardmode()
    
    else:
        print("Invalid input. Please enter a valid number.")
        numguesser()


# Run the game
numguesser()
