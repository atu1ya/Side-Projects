import random

def playnumguesser(coins):
    """
    This is a simple number guessing game. The user has to guess a random number between 1 and 20. The user has 3 chances to guess the number, and the game ends when the user guesses the correct number or runs out of chances.
    """
    user_input_lower = int(input("What is the lower number in the range you would like to guess from? "))
    user_input_upper = int(input("What is the higher number in the range you would like to guess from? "))
    user_input_chances = int(input("How many chances would you like to have to guess the number? "))
    user_input_bet = int(input("How many coins would you like to bet? "))

    number = random.randint(user_input_lower, user_input_upper)  # Random number to be guessed
    chances = user_input_chances  # Number of chances to guess the number

    while chances > 0:
        coins -= user_input_bet
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
            winvalue = user_input_bet + (user_input_bet * ((user_input_upper - user_input_lower) * 0.01) * (chances * 10))
            coins += winvalue
            realwinvalue = winvalue - user_input_bet
            print(f"You have won {realwinvalue} coins! You now have {coins} coins.")
            userinput1 = input("Press enter to play again or type 'Quit' to exit.")
            if userinput1.lower() == 'quit':
                print("Thanks for playing! You have quit the game.")
                break
            else:
                playnumguesser(coins)

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

        chances -= 1  # Decrement the chances after each guess

    if chances == 0:
        # If the user runs out of chances
        print(f"Sorry! You have run out of chances. The number I was thinking of was {number}. Better luck next time!")
        print(f"You have {coins} coins.")
        userinput2 = input("Press enter to play again or type 'Quit' to exit.")
        if userinput2.lower() == 'quit':
            print("Thanks for playing! You have quit the game.")
            quit = True
            return
        else:
            playnumguesser(coins)

    #would you like to play again? if yes playagain(coins), if no thanks for playing.


def numguesser():
    """
    This is a simple number guessing game. The user has to guess a random number between 1 and 20. The user has 3 chances to guess the number, and the game ends when the user guesses the correct number or runs out of chances.
    """
    print("Welcome to Atulya's Number Guesser Game!")
    print("You get to choose how hard the game is. The bigger the range of numbers, the better the reward.")
    print("You start with 20 coins, and can bet up to the amount of coins you currently have")
    print("Press enter to play the game, or type quit at any time to exit.")

    coins = 20
    quit = False
    while coins > 0 and not quit:
        print(f"You have {coins} coins.")
        useresponse = input("Press enter to play or type 'Quit' to exit: ")

        # Check if user wants to quit
        if useresponse.lower() == 'quit':
            print("Thanks for playing! You have quit the game.")
            quit = True
            break
        else:
            playnumguesser(coins)


numguesser()
    
