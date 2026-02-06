#Hangman Game

import random

words = ["apple", "mango", "tiger", "chair", "house"]

word = random.choice(words)

guessed_letters = []
chances = 6

print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        chances -= 1
        print("Wrong guess!")
        print("Remaining chances:", chances)

else:
    print("\n Game Over!")
    print("The word was:", word)

