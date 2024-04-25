import random # Import random module to generate random numbers for the slots

# Define functions for each event in the game
def jackpot(coins):
    """
    This function is called when all 3 slots are equal, and adds 10 coins to the user's total. 
    """
    print("JACKPOT!! \n You win 10 coins!")
    print("If you want to play again, press enter. If you want to quit, type 'quit'.")
    coins += 10
    return coins
    
def win(coins):
    """
    This function is called when two slots are equal, and adds 7 coins to the user's total.
    """
    print("You win 7 coins!")
    coins += 7
    return coins
    
def lose(coins):
    """
    This function is called when no slots are equal, and subtracts 5 coins from the user's total.
    """
    print("You lose! Try again. If you want to play again, press enter. If you want to quit, type 'quit'.")
    coins -= 5
    return coins


# Define the main game function
def slots_game():
    """
    
    This is a simple slots game, that initialises the user with 20 coins. The user can play the game by pressing enter, and it ends when the user does not have enough coins to play again
    or when the user types 'quit'. The user can win 7 coins if 2 of the slots are equal, and 10 coins if all 3 slots are equal. The user loses 5 coins every time they play the game.

    """
    print("Welcome to Atulya's Slots Game!")
    print('It costs 5 coins to play the game. If 2 of the slots are equal, you win 7 coins. If all 3 slots are equal, you win 10 coins.')
    
    
    coins = 20 # Initialise number of coins as 20
    quit = False # Initialise quit as false, so as to run game until user types 'quit'

    # Start game asking user if they want to play or quit
    while coins > 5 and not quit:
        print(f"You have {coins} coins.")
        useresponse = input("Press enter to play or type 'Quit' to exit: ")

        # Check if user wants to quit
        if useresponse.lower() == 'quit':
            print("Thanks for playing! You have quit the game.")
            quit = True
            break
        
        # Charge user for playing the game
        coins -= 5

        # Generate random numbers for each slot
        slot1 = random.randint(1, 9)
        slot2 = random.randint(1, 9)
        slot3 = random.randint(1, 9)
        print(f"{slot1} {slot2} {slot3}")


        # Call each function based on the result of the slots

        if slot1 == slot2 == slot3:
            coins = jackpot(coins)

        elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
            coins = win(coins)

        else:
            lose(coins)
            

    # Check if user has enough coins to play the game, if not, end the game
    if coins < 5:
        input("You are out of coins. Game over! I am making you quit the game. Do better next time!")
        if not quit:
            print("Thanks for playing!")
        else:
            print("Thanks for playing! You have quit the game.")

slots_game()
