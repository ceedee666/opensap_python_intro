# Wordle in Python

Your task for the final assignment is to implement a [Wordle](https://en.wikipedia.org/wiki/Wordle)
clone in Python. The basis for you version of Wordle is the file
`5_letter_words.txt` [[1]](https://www-cs-faculty.stanford.edu/~knuth/sgb.html).
It contains more than 5.700 5 letter words. In order to build your
version of Wordle perform the following steps:

1. Implement a function `word_list()` that reads the `5_letter_words.txt` file and returns a list
   of the words in the file.
1. Implement a function `random_word()` that takes a list of words as a parameter and returns a random word
   from this list. This random word is the one, the user of Wordle has to find. 
1. Implement a function `is_real_word()` that takes a guess and a word list and returns `True` if
   the word is in the word list and `False` otherwise.
1. Implement a function `check_guess()`that takes two parameters. The first is the guessed word and the second is the
   word the user has to find. `check_guess()` returns a string containing the following characters:
   - `X` for each character in the guess that is at the correct position.
   - `O` for each character in the guess that is in the word but not at the correct position. 
   - `_` for each character in the guess that is not part of the word.
    For example, `check_guess("birds", "words")` should return `__XXX`.
   - If a letter is used twice in the guess word and exists only once in the word to be found, then only one letter in the return string is marked. In case one of the two letters is positioned correctly, then this letters is marked with an `X` in th return string.
   For example, `check_guess("carat", "train")` should return `_OO_O`.
   Another example, `check_guess("taunt", "train")` should return `XO_O_`
1. Implement a function `next_guess()` that takes a word list as a parameter. The function asks the user
   for a guess converts the guess to lower case and checks if the guess is in the word list. If yes, the guess is returned. If not the program asks the user
   for another guess.
1. Implement a function `play()` that:

    - uses `word_list` and `random_word` to select a random 5 letter word.
    - Asks the user for a guess using the `next_guess` function.
    - Each guess is checked using the `check_guess` function and the result is shown to the user.
    - If the users guesses the right word with six guesses or less, the user wins.
    - Otherwise the user loses.

Below is an example execution of the program:

    Please enter a guess: aaaaa
    That's not a real word!
    Please enter a guess: bbbbb
    That's not a real word!
    Please enter a guess: hello
    ____O
    Please enter a guess: world
    _OO__
    Please enter a guess: story
    O_OO_
    Please enter a guess: hours
    _O_OO
    Please enter a guess: works
    _OO_O
    Please enter a guess: crops
    _OO_O
    You lost!
    The word was: visor

<br/>

And here is another example execution of the program:

    Please enter a guess: hello
    OO___
    Please enter a guess: there
    XXX_X
    Please enter a guess: these
    XXXXX
    You won!
