Problem Description:
Save the Watermelon is a word-guessing game
for anyone who likes word puzzles such as hangman. The
computer randomly chooses a secret word
and the player must guess the letters before
running out of watermelon slices.

Game Rules:
	•	The computer randomly selects a word and the amount of letters are displayed with underscores.
	•	 The player guesses one letter at a time.
	•	 Correct guesses reveal all matching letters.
	•	 Incorrect guesses remove one slice.
	•	Invalid and repeated guesses do not remove slices.
	•	The player wins by revealing the word.
	•	The player loses when zero slices remain.

Program Data:
	•	secret_word: stores the selected word.
	•	guessed_letters: stores letters already guessed.
	•	remaining_slices: stores how many slices are left.
	•	displayed_word: shows revealed letters and the rest of the underscores that are still to be guessed.
	•	word_list: stores possible words.

Program Organization:
	•	choose_word(): randomly selects a word
	•	display_word(): displays the hidden word with one underscore per letter
	•	ask_guess(): asks the player for a letter guess
	•	play_game(): controls a round of the game
	•	main(): starts the game until end and repeats if player chooses

Program Flow
Start > 
Select hidden word > 
Display the hidden word with underscores > 
Ask player to guess a letter > 
Check letter guess is valid or if the letter was already guessed > 
Reveal correct letters or remove a slice after an incorrect guess > 
Repeat until the word is revealed or slices are all used > 
Display “You won” if player reveals word or “Lost. Good try!” if the player uses up slices without revealing the word > 
Ask the player if they want to play again > 
End the program if the player says no, if the player says yes, repeat same steps.

