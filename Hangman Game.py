
import random

# List of 5 predefined words
words = ["python", "computer", "program", "science", "college"]

# Randomly select a word
secret_word = random.choice(words)

# Variables
guessed_letters = []
attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

# Game loop
while attempts > 0:

    # Display the word with guessed letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect attempts left:", attempts)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word!")
        break

    # Take input from player
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet!")
        continue

    # Check duplicate guesses
    if guess in guessed_letters:
        print("You have already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

# Final result
if attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", secret_word)
