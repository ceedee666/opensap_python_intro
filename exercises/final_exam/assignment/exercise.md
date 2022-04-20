# Wordle in Python

Your task for the final assignment is to implement a [Wordle](https://en.wikipedia.org/wiki/Wordle)
clone in Python. The basis for you version of Wordle is the files
`5_letter_words.txt`. It contains more than 10.000 5 letter words. In order op build your
version of Wordle preform the following steps:

1. Implement a function `word_list()` that reads the `5_letter_words.txt` file and returns a list
   of the words in the file.
1. Implement a function `random_word()` that takes a list of words as a parameter and returns a random word
   from this list.
1. Implement a function `check_guess()`that takes two parameters. The fist is the guess and the second the
   word the user needs to find. `check_guess()` returns a string containing the following characters:

- `X` for each character in the guess that is at the correct position
- `O` for each character in the guess that is in the word but not at the correct position
- `_` for each character in the guess that is not part of the word.
  For example, `check_guess("birds", "words")` should return `__XXX`.

1. Implement a function `play()` that:

- uses `word_list`and `random_word` to select a random 5 letter word.
- Asks the user for a guess.
- Each guess is checked using the `check_guess` function and the result is shown to the user.
- If the users guesses the right word with six guesses or less, the user wins.
- Otherwise the user loses.

Below is an example execution of your program:
