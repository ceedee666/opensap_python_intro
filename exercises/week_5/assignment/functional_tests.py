import contextlib
import io
import os
import random
import string
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
    def encrypt_letter(self, letter, shift):
        abc = "abcdefghijklmnopqrstuvwxyz"
        ind = abc.index(letter)
        ind = (ind + shift) % 26
        secret_letter = abc[ind]
        return secret_letter

    def calculate_shifts(self, letter):
        abc = "abcdefghijklmnopqrstuvwxyz"
        ind = abc.index(letter)
        return ind

    def encrypt_text(self, text, keyword):
        text = text.lower()
        keyword = keyword.lower()

        encrypted_text = ""

        for i in range(len(text)):
            key_letter = keyword[i % len(keyword)]
            shift = self.calculate_shifts(key_letter)
            if text[i].isalpha():
                encrypted_text += self.encrypt_letter(text[i], shift)
            else:
                encrypted_text += text[i]
        return encrypted_text


class Testing(TestCase):
    @mock.patch("builtins.input", create=True)
    def test_output(self, mocked_input):

        text = "Rock 'n' Roll High School"
        keyword = "Ramones"
        mocked_input.side_effect = [text, keyword]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()
        expected_out = "iooy 'f' dcyp yisv wuyoaz"

        self.assertIn(
            expected_out,
            output,
            f"The input should be encrypted correctly. For a keyword {keyword} and the input {text} the expected output is {expected_out}. The output of your program was: {output}",
        )

        keyword = "".join(random.sample(string.ascii_lowercase, 5))
        text = "Python is cool"
        mocked_input.side_effect = [text, keyword]

        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()
        expected_out = ReferenceImplementation().encrypt_text(text, keyword)

        self.assertIn(
            expected_out,
            output,
            f"The input should be encrypted correctly. For a keyword {keyword} and the input {text} the expected output is {expected_out}. The output of your program was: {output}",
        )

    @mock.patch("builtins.input", create=True)
    def test_encrpyt_text(self, mocked_input):
        mocked_input.side_effect = ["dummy", "dummy"]
        with capture():
            import exercise as user

        keyword = "python"
        text = "!.;,123456789"
        result = user.encrypt_text(text, keyword)

        self.assertEqual(
            text,
            result,
            f"Special characters should be ignored and not changed by the function encrypt_text(). For the input {text} and the keyword {keyword} the output of your encrypt_text() function was: {result}",
        )

        keyword = "python"
        text = "1 2 3 4 5 6 7 8 9"
        result = user.encrypt_text(text, keyword)

        self.assertEqual(
            text,
            result,
            f"Spaces should not be removed the the function encrypt_text(). For the input {text} and the keyword {keyword} the output of your encrypt_text() function was: {result}",
        )

        keyword = "aaaaa"
        text = "Python is cool"
        expected_result = "python is cool"
        result = user.encrypt_text(text, keyword)

        self.assertEqual(
            result,
            expected_result,
            f"A text should be encrypted correctly by your function encrypt_text(). For the input {text} and the keyword {keyword} the output of your encrypt_text() function was: {result}",
        )

        keyword = "".join(random.sample(string.ascii_lowercase, 5))
        text = "Python is cool"
        expected_result = ReferenceImplementation().encrypt_text(text, keyword)
        result = user.encrypt_text(text, keyword)

        self.assertEqual(
            result,
            expected_result,
            f"A text should be encrypted correctly by your function encrypt_text(). For the input {text} and the keyword {keyword} the output of your encrypt_text() function was: {result}",
        )

    @mock.patch("builtins.input", create=True)
    def test_shift_zero(self, mocked_input):

        text = "Python is cool!"
        keyword = "aaaaa"
        mocked_input.side_effect = [text, keyword]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()
        expected_out = "python is cool!"

        self.assertIn(
            expected_out,
            output,
            f"The input should be encrypted correctly. For a keyword {keyword} and the input {text} the expected output is {expected_out}. The output of your program was: {output}",
        )

    @mock.patch("builtins.input", create=True)
    def test_calculate_shift(self, mocked_input):
        mocked_input.side_effect = ["dummy", "dummy"]
        with capture():
            import exercise as user

        letter = "b"
        result = user.calculate_shifts(letter)

        expected_out = 1
        self.assertEqual(
            expected_out,
            result,
            f"The result of the function calculate_shift() is not correct. For the letter {letter} the result should be {expected_out}.",
        )

        letter = "m"
        result = user.calculate_shifts(letter)

        expected_out = 12
        self.assertEqual(
            expected_out,
            result,
            f"The result of the function calculate_shift() is not correct. For the letter {letter} the result should be {expected_out}.",
        )

    @mock.patch("builtins.input", create=True)
    def test_encrypt_letter(self, mocked_input):
        mocked_input.side_effect = ["dummy", "dummy"]
        with capture():
            import exercise as user

        letter = "b"
        shift = 10
        result = user.encrypt_letter(letter, shift)

        expected_out = "l"
        self.assertEqual(
            expected_out,
            result,
            f"The result of the function encrypt_letter() is not correct. For the letter {letter} and the shift {shift} the result should be {expected_out}.",
        )

        letter = "w"
        shift = 10
        result = user.encrypt_letter(letter, shift)

        expected_out = "g"
        self.assertEqual(
            expected_out,
            result,
            f"The result of the function encrypt_letter() is not correct. For the letter {letter} and the shift {shift} the result should be {expected_out}.",
        )

        letter = "1"
        shift = 10
        result = user.encrypt_letter(letter, shift)

        expected_out = "1"
        self.assertEqual(
            expected_out,
            result,
            f"The result of the function encrypt_letter() is not correct. Special letters should not be changed. For the letter {letter} and the shift {shift} the result should be {expected_out}.",
        )

        letter = "?"
        shift = 10
        result = user.encrypt_letter(letter, shift)

        expected_out = "?"
        self.assertEqual(
            expected_out,
            result,
            f"The result of the function encrypt_letter() is not correct. Special letters should not be changed. For the letter {letter} and the shift {shift} the result should be {expected_out}.",
        )


if __name__ == "__main__":
    unittest.main()
