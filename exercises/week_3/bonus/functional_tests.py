import contextlib
import io
import os
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


class Testing(TestCase):
    @mock.patch("builtins.input", create=True)
    def test_shift_value(self, mocked_input):
        input = "python"
        mocked_input.side_effect = ["36", input]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()

        expected_out = "between 0 and 25"
        self.assertIn(
            expected_out,
            output,
            f"Your program should only accept shift values between 0 and 25!",
        )

        input = "python"
        mocked_input.side_effect = ["-3.2", input]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()

        expected_out = "between 0 and 25"
        self.assertIn(
            expected_out,
            output,
            f"Your program should only accept shift values between 0 and 25!",
        )

        input = "python"
        mocked_input.side_effect = ["-3.2", input]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()

        expected_out = "between 0 and 25"
        self.assertIn(
            expected_out,
            output,
            f"Your program should only accept integers as the shift value!",
        )

    @mock.patch("builtins.input", create=True)
    def test_ignore_special_chars(self, mocked_input):
        input = "!.;,"
        mocked_input.side_effect = ["5", input]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()

        expected_out = input
        self.assertIn(
            expected_out,
            output,
            f"Special characters should be ignored and not changed by you program. For the input {input} the output of your program was: {output}",
        )

    @mock.patch("builtins.input", create=True)
    def test_keep_spaces(self, mocked_input):
        input = "! - , !"
        mocked_input.side_effect = ["5", input]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()
        expected_out = input

        self.assertIn(
            expected_out,
            output,
            f"Spaces should not be removed from the output. For the input {input} the output of your program was: {output}",
        )

    @mock.patch("builtins.input", create=True)
    def test_correct_encryption(self, mocked_input):

        shift = "5"
        input = "hey ho lets go"
        mocked_input.side_effect = [shift, input]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()
        expected_out = "mjd mt qjyx lt"

        self.assertIn(
            expected_out,
            output,
            f"The input should be encrypted correctly. For a shift value of {shift} and the input {input} the expected output is {expected_out}. The output of your program was: {output}",
        )

        shift = "15"
        input = "obi-wan kenobi"
        mocked_input.side_effect = [shift, input]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()
        expected_out = "dqx-lpc ztcdqx"

        self.assertIn(
            expected_out,
            output,
            f"The input should be encrypted correctly. For a shift value of {shift} and the input {input} the expected output is {expected_out}. The output of your program was: {output}",
        )

    @mock.patch("builtins.input", create=True)
    def test_shift_zero(self, mocked_input):

        shift = "0"
        input = "zaphod beeblebrox"
        mocked_input.side_effect = [shift, input]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()
        expected_out = "zaphod beeblebrox"

        self.assertIn(
            expected_out,
            output,
            f"The input should not be changed when a shift value of 0 is used. For the input {input} the expected output is {expected_out}. The output of your program was: {output}",
        )

    @mock.patch("builtins.input", create=True)
    def test_shift_25(self, mocked_input):

        shift = "25"
        input = "marvin, the paranoid android"
        mocked_input.side_effect = [shift, input]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()
        expected_out = "lzquhm, sgd ozqzmnhc zmcqnhc"

        self.assertIn(
            expected_out,
            output,
            f"The input should be encrypted correctly. For a shift value of {shift} and the input {input} the expected output is {expected_out}. The output of your program was: {output}",
        )


if __name__ == "__main__":
    unittest.main()
