import random


def word_list(path="./5_letter_words.txt"):
    with open(path) as f:
        lines = f.readlines()
    return [l.strip() for l in lines]


def random_word(word_list):
    return random.choice(word_list)


def check_guess(guess, word):
    result = ""
    for i, l in enumerate(guess):
        if l == word[i]:
            result += "X"
        elif l in word:
            result += "O"
        else:
            result += "_"
    return result


def play():
    word = random_word(word_list())

    won = False
    i = 0
    while i < 6 and not (won):
        guess = input("Please enter a guess: ")
        result = check_guess(guess, word)
