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



from logic import choose_word, display_word, ask_guess


def play_game():

    secret_word = choose_word()
    guessed_letters = set()
    remaining_slices = 6

    print("Welcome to Save the Watermelon!")

    while remaining_slices > 0:

        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Remaining slices:", remaining_slices)

        guess = ask_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct!")

        else:
            remaining_slices -= 1
            print("Incorrect!")
            print("Take away 1 slice from remaining slices.")
            print("Remaining slices:", remaining_slices)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nWord:", display_word(secret_word, guessed_letters))
            print("You won! The watermelon has been saved!")
            return

    print("\nLost. Good try!")
    print("The secret word was:", secret_word)

def main():


    while True:

        play_game()

        while True:
            play_again = input(
                "\nWould you like to play again? (yes/no): "
            ).strip().lower()

            if play_again == "yes" or play_again == "no":
                break

            print("Please enter yes or no.")

        if play_again == "no":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
