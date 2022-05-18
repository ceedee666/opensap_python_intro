import random


def word_list(path="./5_letter_words.txt"):
    with open(path) as f:
        lines = f.readlines()
    return [l.strip() for l in lines]


def random_word(word_list):
    return random.choice(word_list)


def check_guess(guess, word):
    word_list = list(word)
    result = ["_"] * len(word)

    # check for exact matches chars
    for i, l in enumerate(guess):
        if l == word_list[i]:
            result[i] = "X"
            word_list[i] = " "

    # check for chars are wrong position
    for i, l in enumerate(guess):
        if l in word_list:
            if result[i] != "X":
                result[i] = "O"
                word_list[word_list.index(l)] = " "

    return "".join(result)


def is_real_word(guess, word_list):
    return guess in word_list


def next_guess(word_list):
    guess = ""
    in_word_list = False
    while not in_word_list:
        guess = input("Please enter a guess: ")
        guess = guess.lower()

        if is_real_word(guess, word_list):
            in_word_list = True
        else:
            print("That's not a real word!")
    return guess


def play():
    five_letter_words = word_list()
    secret_word = random_word(five_letter_words)

    won = False

    for _ in range(6):
        guess = next_guess(five_letter_words)
        result = check_guess(guess, secret_word)
        print(result)
        if result == "XXXXX":
            won = True
            break

    if won:
        print("You won!")
    else:
        print("You lost!")
        print("The word was:", secret_word)


if __name__ == "__main__":
    play()
