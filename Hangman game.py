
import random


def getword(difficulty):
    if difficulty == "easy":
        words =  ["Cat", "Dog", "Tree", "Fish", "Bird", "Book", "Food", 
                  "Cake", "Car", "Ball", "Milk", "Moon", "Star", "Rain", "House"]

    elif difficulty == "medium":
        words = ["Laptop", "Jungle", "Rocket", "Helmet", "Python", "Garden", "Planet", "Oxygen", 
                 "Pumpkin", "Whistle", "Pyramid", "Thirsty", "Lantern", "Circus", "Sandwich"]
        
    elif difficulty == "hard":
        words =  ["Exotic", "Venture", "Whisper", "Glacier", "Orchestra", "Contraption", "Dictionary", "Phenomenon", 
                  "Adventure", "Gallery", "Musician", "Resilient", "Symphony", "Evaluate", "Juxtapose"]
        
    else:
        print("Invalid difficulty! Please choose easy, medium, or hard!")
        return
    return random.choice(words)

def printword(word):
    for i in range(len(word)):
        print("_", end=" ")
    print()

def play_round(word, guesses, points):
    guessed_letters = []
    correct_letters = []
    while guesses > 0:
        print("Guess a letter: ")
        guess = input().upper()
        if guess in guessed_letters:
            print("You already guessed that letter! Try again!")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print("Correct!")
            correct_letters.append(guess)
            print("Here is the word: ")
            for letter in word:
                if letter in correct_letters:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print()
            if len(correct_letters) == len(word):
                print("Congratulations! You guessed the word!")
                if len(word) < 5:
                    points += 5
                elif 5 <= len(word) < 8:
                    points += 7
                else:
                    points += 10
                print("You have " + str(points) + " points!")
                print("Would you like to play another round? (yes/no)")
                play_again = input()
                if play_again == "yes":
                    return points
                else:
                    print("Goodbye!")


                return
        else:
            print("Incorrect!")
            guesses -= 1
            print("You have " + str(guesses) + " guesses left!")
    print("You ran out of guesses! The word was " + word + ". Game Over!")
    return


def hangman():
    print("Welcome to Atulya's Hangman Game!")
    print("You get to pick how many guesses you get, and how hard the word is to guess!")
    print("The harder the word, and the less guesses you have, the more points you get!")
    print("If you don't guess the word the game ends :( ")
    print("Let's see what the highest score you can get is! Good Luck!")
    quit = False
    points = 0
    while not quit:
        print("Would you like to play a game? (yes/no)")
        play_game = input().lower()
        if play_game == "yes":
            print("Great! Let's get started!")
            print("How many guesses would you like to have?")
            guesses = int(input())
            print("How hard would you like the word to be? (easy/medium/hard)")
            difficulty = input().lower()
            word = getword(difficulty)
            print("The word has been chosen! Let's get started!")
            print("Here is the word: ")
            printword(word)
            print("You have " + str(guesses) + " guesses left!")
            play_round(word, guesses, points)
        else:
            print("Goodbye!")
            quit = True


hangman()
