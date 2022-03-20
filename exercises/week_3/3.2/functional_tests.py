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
    def test_output_not_changed(self, mocked_input):
        input = "noting to see here"
        mocked_input.side_effect = [input]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()

        expected_out = input
        self.assertEqual(
            expected_out,
            output,
            "The output of your program is not correct.",
        )

    @mock.patch("builtins.input", create=True)
    def test_example_sentence(self, mocked_input):
        input = "I'm so excited to learn python"
        mocked_input.side_effect = [input]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()
        expected_out = "I'm so 🤩 to learn 🐍"

        self.assertEqual(
            expected_out,
            output,
            "The output of your program is not correct.",
        )

    @mock.patch("builtins.input", create=True)
    def test_random_words(self, mocked_input):
        input = "happy heart smile rotfl"
        mocked_input.side_effect = [input]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()
        expected_out = "😃 😍 😊 🤣"

        self.assertEqual(
            expected_out,
            output,
            "The output of your program is not correct.",
        )


if __name__ == "__main__":
    unittest.main()
