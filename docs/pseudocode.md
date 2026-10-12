Pseudocode:

START GAME

FUNCTION choose_word
Word will be randomly selected from word list 
Chosen word will be stored as secret_word
RETURN secret_word
END FUNCTION

FUNCTION display_word
FOR each letter in secret_word
IF the letter is in guessed_letters
Display the correctly guessed letter
ELSE Display an underscore in place of the letter
END FUNCTION 

FUNCTION ask_guess
Ask the player to enter a letter
Remove extra spaces at the beginning or end
Convert player's letter to lowercase to account for both capital and lowercase lettering
IF the input does not contain exactly one character
DISPLAY  "Please enter only one letter."
ELSE IF the input is not an alphabetic letter
DISPLAY "Invalid input. Please enter a letter."
ELSE IF the letter is already in guessed_letters
DISPLAY "You already guessed that letter."
ELSE
RETURN the valid letter.
END IF
UNTIL the player enters a valid letter that has not already been guessed
REPEAT 
END FUNCTION

FUNCTION play_game
choose_word will randomly choose a word from word_list
Empty collection called guessed_letters will be created
remaining_slices will be set to 6
PRINT “Welcome to Save the Watermelon!”
display_word will show underscores matching up with selected words letter amount
remaining_slices will show quantity of guesses (slices) allowed
Call ask_guess to receive a letter guess
guessed_letters will add letter to collection
IF guessed letter is in secret_word 
PRINT “Correct!”
Reveal every space letter is in secret_word 
No slices are subtracted 
ELSE
PRINT “Incorrect!”
Take away 1 slice from remaining_slices
END IF
Every letter in secret_word is included in guessed_letters
Show completely revealed word
PRINT "You won! The watermelon has been saved!"
 END the game.

ELSE
IF remaining_slices equals 0
AND the word has not been fully revealed
PRINT "Lost. Good try!"
Reveal secret_word
   
END FUNCTION

FUNCTION main
Play one round of game
Ask if player would like to play again
UNTIL player chooses they do not want to play again
REPEAT
END FUNCTION

END PROGRAM
