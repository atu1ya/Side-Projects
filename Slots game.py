# Add comments throughout the text to explain the code
# Current bugs to fix, need to press enter 3 times to play the game, and the game ends when the user types 'quit' instead of when the user does not have enough coins to play again.
# Ask the user how many coins they want to start with, and if they want to play again after they run out of coins.

import random

def slots_game():
    """
    
    This is a simple slots game, that initialises the user with 20 coins. The user can play the game by pressing enter, and it ends when the user does not have enough coins to play again
    or when the user types 'quit'. The user can win 7 coins if 2 of the slots are equal, and 10 coins if all 3 slots are equal. The user loses 5 coins every time they play the game.

    """
    print("Welcome to Atulya's Slots Game!")
    print('It costs 5 coins to play the game. If 2 of the slots are equal, you win 7 coins. If all 3 slots are equal, you win 10 coins.')
    print("You have 20 coins.")
    print("Press enter to play the game.")
    coins = 20
    while coins > 5:
        print(f"You have {coins} coins.")
        input()
        if input() == 'quit':
            print("Thanks for playing! You have quit the game.")
            break

        coins -= 5
        slot1 = random.randint(1, 9)
        slot2 = random.randint(1, 9)
        slot3 = random.randint(1, 9)
        print(f"{slot1} {slot2} {slot3}")

        if slot1 == slot2 == slot3:
            print("!!JACKPOT!! \n You win 10 coins!")
            print("If you want to play again, press enter. If you want to quit, type 'quit'.")
            coins += 10
            if input() == 'quit':
                print("Thanks for playing! You have quit the game.")
                break

        elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
            print("You win 7 coins!")
            coins += 7
            print("If you want to play again, press enter. If you want to quit, type 'quit'.")
            if input() == 'quit':
                print("Thanks for playing! You have quit the game.")
                break

        else:
            print("You lose! Try again. If you want to play again, press enter. If you want to quit, type 'quit'.")
            if input() == 'quit':
                print("Thanks for playing! You have quit the game.")
                break

    if coins <= 5:
        print("You are out of coins. Game over! I am making you quit the game. Do better next time!")
        print("Thanks for playing!")

slots_game()