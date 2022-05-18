import contextlib
import io
import os
import random
import sys
import unittest
from unittest import TestCase, mock

sys.modules["assess"] = sys.modules[__name__]
dirname = os.path.dirname(__file__)


@contextlib.contextmanager
def capture():
    global captured_out
    import sys

    oldout, olderr = sys.stdout, sys.stderr
    try:
        out = [io.StringIO(), io.StringIO()]
        captured_out = out
        sys.stdout, sys.stderr = out
        yield out
    finally:
        sys.stdout, sys.stderr = oldout, olderr


@contextlib.contextmanager
def trace(t):
    try:
        if t:
            t.start()
        yield
    finally:
        if t:
            t.stop()


def runcaptured(tracing=None, variables=None):
    filename = "exercise.py"
    with open(filename) as f:
        source = f.read()
        c = compile(source, filename, "exec")
        with capture() as out, trace(tracing):
            if variables is None:
                variables = {}
            exec(c, variables)
        return source, out[0], out[1], variables


class ReferenceImplementation:
    def random_word(self, word_list):
        return random.choice(word_list)

    def check_guess(self, guess, word):
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

    def is_real_word(self, guess, word_list):
        return guess in word_list

    def word_list(self, path="./5_letter_words.txt"):
        with open(path) as f:
            lines = f.readlines()
        return [l.strip() for l in lines]


class Testing(TestCase):
    @mock.patch("builtins.open", create=True)
    def test_word_list(self, mock_open):
        mock_open.return_value = io.StringIO("aaaaa\nbbbbb\nccccc")
        with capture():
            import exercise as user

        result = user.word_list()
        self.assertEqual(
            result,
            ["aaaaa", "bbbbb", "ccccc"],
            "The function word_list should return a list of words from the input file. Trailing '\n' should be removed",
        )

    @mock.patch("builtins.input", create=True)
    def test_random_word(self, mock_input):
        mock_input.side_effect = ["world"] * 30
        with capture():
            import exercise as user

        result = user.random_word(["aaaaa"])
        expected_out = "aaaaa"
        self.assertEqual(
            expected_out,
            result,
            "The result of the function random_word is not correct. For a word list containing a single word the function should return that word.",
        )

        test_word_list = [
            "which",
            "there",
            "their",
            "about",
            "would",
            "these",
        ]
        result = user.random_word(test_word_list)
        self.assertIn(
            result,
            test_word_list,
            "The result of the function random_word is not correct. The function should return a word from the list of words.",
        )

        result_list = [user.random_word(test_word_list) for _ in range(10)]
        result_set = set(result_list)
        self.assertGreaterEqual(
            len(result_set),
            1,
            "The result of the function random_word is not correct. The function should return different words for the word list.",
        )

    @mock.patch("builtins.input", create=True)
    def test_check_guess(self, mock_input):
        mock_input.side_effect = ["world"] * 30
        with capture():
            import exercise as user

        result = user.check_guess("aaaaa", "bbbbb")
        expected_out = "_____"
        self.assertEqual(
            expected_out,
            result,
            "The result of the function check_guess is not correct. The function should return '_____' for a guess of 'aaaaa' and the word 'bbbbb'.",
        )

        result = user.check_guess("bbbbb", "bbbbb")
        expected_out = "XXXXX"
        self.assertEqual(
            expected_out,
            result,
            "The result of the function check_guess is not correct. The function should return 'XXXXX' for a guess of 'bbbbb' and the word 'bbbbb'.",
        )

    @mock.patch("builtins.input", create=True)
    def test_check_guess_2(self, mock_input):
        mock_input.side_effect = ["world"] * 30
        with capture():
            import exercise as user

        result = user.check_guess("world", "words")
        expected_out = "XXX_O"
        self.assertEqual(
            expected_out,
            result,
            "The result of the function check_guess is not correct. The function should return 'XXX_O' for a guess of 'world' and the word 'words'.",
        )

        result = user.check_guess("whole", "white")
        expected_out = "XX__X"
        self.assertEqual(
            expected_out,
            result,
            "The result of the function check_guess is not correct. The function should return 'XX__X' for a guess of 'whole' and the word 'white'.",
        )

    @mock.patch("builtins.input", create=True)
    def test_check_guess_3(self, mock_input):
        mock_input.side_effect = ["world"] * 30
        with capture():
            import exercise as user
        result = user.check_guess("cocoa", "taboo")
        expected_out = "_O_XO"
        self.assertEqual(
            expected_out,
            result,
            "The result of the function check_guess is not correct. The function should return '_O_XO' for a guess of 'cocoa' and the word 'taboo'.",
        )
        result = user.check_guess("moons", "taboo")
        expected_out = "_OO__"
        self.assertEqual(
            expected_out,
            result,
            "The result of the function check_guess is not correct. The function should return '_OO__' for a guess of 'moons' and the word 'taboo'.",
        )

        result = user.check_guess("carat", "train")
        expected_out = "_OO_O"
        self.assertEqual(
            expected_out,
            result,
            "The result of the function check_guess is not correct. The function should return '_OO_O' for a guess of 'carat' and the word 'train'.",
        )

        result = user.check_guess("carat", "taboo")
        expected_out = "_X__O"
        self.assertEqual(
            expected_out,
            result,
            "The result of the function check_guess is not correct. The function should return '_X__O' for a guess of 'carat' and the word 'taboo'.",
        )

        result = user.check_guess("raver", "heres")
        expected_out = "O__X_"
        self.assertEqual(
            expected_out,
            result,
            "The result of the function check_guess is not correct. The function should return 'O__X_' for a guess of 'raver' and the word 'heres'.",
        )

    @mock.patch("builtins.input", create=True)
    def test_check_guess_random_word(self, mock_input):
        mock_input.side_effect = ["world"] * 30
        with capture():
            import exercise as user
        reference = ReferenceImplementation()
        word_list = reference.word_list()
        guess = reference.random_word(word_list)
        secret_word = reference.random_word(word_list)
        expected_out = reference.check_guess(guess, secret_word)

        result = user.check_guess(guess, secret_word)
        self.assertEqual(
            expected_out,
            result,
            f"The result of the function check_guess is not correct. The function should return '{expected_out}' for a guess of '{guess}' and the word '{secret_word}'.",
        )

    @mock.patch("builtins.input", create=True)
    def test_is_real_word(self, mock_input):
        mock_input.side_effect = ["world"] * 30
        with capture():
            import exercise as user

        test_word_list = [
            "which",
            "there",
            "their",
            "about",
            "would",
            "these",
        ]
        result = user.is_real_word("aaaaa", test_word_list)
        self.assertFalse(
            result,
            "The result of the function is_real_word is not correct. The function should return False for a word that is not in the list of words.",
        )

        result = user.is_real_word("about", test_word_list)
        self.assertTrue(
            result,
            "The result of the function is_real_word is not correct. The function should return True for a word that is in the list of words.",
        )

    @mock.patch("builtins.input", create=True)
    def test_is_real_word_random(self, mock_input):
        mock_input.side_effect = ["world"] * 30
        with capture():
            import exercise as user
        reference = ReferenceImplementation()
        word_list = reference.word_list()
        word = reference.random_word(word_list)
        expected_out = reference.is_real_word(word, word_list)

        result = user.is_real_word(word, word_list)
        self.assertEqual(
            expected_out,
            result,
            f"The result of the function check_guess is not correct. The function should return '{expected_out}' for a word that is in the list of words.",
        )

    @mock.patch("builtins.print", create=True)
    @mock.patch("builtins.input", create=True)
    def test_next_guess(self, mock_input, mock_print):
        mock_print.return_value = None
        mock_input.side_effect = ["world"] * 30
        with capture():
            import exercise as user

        mock_input.side_effect = ["these"]

        test_word_list = [
            "which",
            "there",
            "their",
            "about",
            "would",
            "these",
        ]

        result = user.next_guess(test_word_list)
        self.assertEqual(
            "these",
            result,
            "The result of the function next_guess is not correct. The function should accept alls words in the word list.",
        )

        mock_input.side_effect = ["aaaaa", "bbbbb", "about"]
        result = user.next_guess(test_word_list)
        self.assertEqual(
            "about",
            result,
            "The result of the function next_guess is not correct. The function should ask for user input until the entered word is in the word list.",
        )

        mock_input.side_effect = ["ABouT", "which"]
        result = user.next_guess(test_word_list)
        self.assertEqual(
            "about",
            result,
            "The result of the function next_guess is not correct. The function should convert the user input to lower case before checking if a valid word was entered.",
        )

    @mock.patch("builtins.open")
    @mock.patch("builtins.input")
    def test_play(self, mock_input, mock_open):

        mock_input.side_effect = ["world"] * 30
        with capture():
            import exercise as user

        mock_input.side_effect = ["which", "there", "these"]
        mock_open.return_value = io.StringIO(
            "which\nthere\ntheir\nabout\nwould\nthese\n"
        )

        with capture() as out:
            with mock.patch("exercise.random_word", return_value="these"):
                user.play()

            result = out[0].getvalue().strip()
            self.assertIn(
                "_X___",
                result,
                "The result of the function play is not correct. The function should print _X___ for a guess of 'which' and the word 'these'.",
            )

            self.assertIn(
                "XXX_X",
                result,
                "The result of the function play is not correct. The function should print XXX_X for a guess of 'there' and the word 'these'.",
            )
            self.assertIn(
                "XXXXX",
                result,
                "The result of the function play is not correct. The function should print XXXXX for a guess of 'these' and the word 'these'.",
            )
            self.assertIn(
                "you won",
                result.lower(),
                "The result of the function play is not correct. The function should print 'You won' when the user guesses the correct word.",
            )

    @mock.patch("builtins.open")
    @mock.patch("builtins.input")
    def test_play_2(self, mock_input, mock_open):

        mock_input.side_effect = ["world"] * 30
        with capture():
            import exercise as user
        mock_input.side_effect = ["which"] * 6
        mock_open.return_value = io.StringIO(
            "which\nthere\ntheir\nabout\nwould\nthese\n"
        )

        with capture() as out:
            with mock.patch("exercise.random_word", return_value="these"):
                user.play()

            result = out[0].getvalue().strip()
            self.assertIn(
                "you lost",
                result.lower(),
                "The result of the function play is not correct. The function should print 'You lost' after six wrong guesses.",
            )

            self.assertIn(
                "these",
                result,
                "The result of the function play is not correct. The function should print the secret word after six wrong guesses.",
            )


if __name__ == "__main__":
    unittest.main()
