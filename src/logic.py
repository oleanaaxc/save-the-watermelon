import random
from words import word_list

def choose_word():

    secret_word = random.choice(word_list)
    return secret_word

def display_word(secret_word, guessed_letters):
  
    displayed_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    return displayed_word.strip()


def ask_guess(guessed_letters):
 
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1:
            print("Please enter only one letter.")

        elif not guess.isascii() or not guess.isalpha():
            print("Invalid input. Please enter a letter.")

        elif guess in guessed_letters:
            print("You already guessed that letter.")

        else:
            return guess
