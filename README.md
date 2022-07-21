# Wordle Solver

Wordle is a fun 5-letter word game based off of the logic game Mastermind.
Every day, there is a new worde puzzle, and I've created a solver for it.

When you run the program, you will be asked for a mode.

Mode 'c' or calculate, takes every word in my words file and prints the frequency of every letter.
This mode also tells you the best starting word - the word comprised of the most popular letters.

Mode 's' or solve, requires you to enter a command to filter the words.
example:
    let's say your first guess is 'early', but only the 'l' was correct, and no other letters were in the word.
    command: "!e !a !r l !y"
    now let's say your next guess is 'build', 'u' is present but in the wrong place, and 'l' and 'd' are correct.
    command: "!b ?u !i l d"
As you can see, you have 5 tokens seperated by spaces which correspond to each letter of your guess.
No preceding character means that the character is correct.
'?' preceding means that the character is present but in the wrong place.
'!' preceding means that the character is not present.

The program will then give you a list of valid guesses, and the best suggestion.


Play Wordle at this link: https://www.powerlanguage.co.uk/wordle/

Credit to https://github.com/dwyl/english-words for providing the original word list that I filtered for the program.
