import ast
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
    def test_right_triangle(self, mocked_input):
        mocked_input.side_effect = ["60", "90", "30"]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()

        expected_out = "right"
        self.assertIn(
            expected_out,
            output.lower(),
            f"The output of your program is not correct. The triangle with the angles 60, 90 and 30 is a right triangle. The output of your program was: {output}",
        )

        expected_out = "obtuse"
        self.assertNotIn
        (
            expected_out,
            output.lower(),
            f"The output of your program is not correct. The triangle with the angles 60, 90 and 30 is not an obtuse triangle. The output of your program was: {output}",
        )

        expected_out = "acute"
        self.assertNotIn
        (
            expected_out,
            output.lower(),
            f"The output of your program is not correct. The triangle with the angles 60, 90 and 30 is not an acute triangle. The output of your program was: {output}",
        )

    @mock.patch("builtins.input", create=True)
    def test_acute_triangle(self, mocked_input):
        mocked_input.side_effect = ["33", "77", "70"]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()

        expected_out = "right"
        self.assertNotIn(
            expected_out,
            output.lower(),
            f"The output of your program is not correct. The triangle with the angles 33, 77 and 70 is not a right triangle. The output of your program was: {output}",
        )

        expected_out = "obtuse"
        self.assertNotIn
        (
            expected_out,
            output.lower(),
            f"The output of your program is not correct. The triangle with the angles 33, 77 and 70 is not an obtuse triangle. The output of your program was: {output}",
        )

        expected_out = "acute"
        self.assertIn
        (
            expected_out,
            output.lower(),
            f"The output of your program is not correct. The triangle with the angles 33, 77 and 70 is an acute triangle. The output of your program was: {output}",
        )

    @mock.patch("builtins.input", create=True)
    def test_obtuse_triangle(self, mocked_input):
        mocked_input.side_effect = ["30", "30", "120"]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()

        expected_out = "right"
        self.assertNotIn(
            expected_out,
            output.lower(),
            f"The output of your program is not correct. The triangle with the angles 30, 30 and 120 is an obtuse triangle. The output of your program was: {output}",
        )

        expected_out = "obtuse"
        self.assertIn
        (
            expected_out,
            output.lower(),
            f"The output of your program is not correct. The triangle with the angles 30, 30 and 120 is an obtuse triangle. The output of your program was: {output}",
        )

        expected_out = "acute"
        self.assertNotIn
        (
            expected_out,
            output.lower(),
            f"The output of your program is not correct. The triangle with the angles 30, 30 and 120 is not an acute triangle. The output of your program was: {output}",
        )

    @mock.patch("builtins.input", create=True)
    def test_not_valid_triangle(self, mocked_input):
        mocked_input.side_effect = ["10", "10", "10"]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()

        expected_out = "not valid"
        self.assertIn(
            expected_out,
            output.lower(),
            f"The output of your program is not correct. The values 10, 10 and 10 are not valid. The output of your program was: {output}",
        )

        mocked_input.side_effect = ["100", "100", "100"]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()

        expected_out = "not valid"
        self.assertIn(
            expected_out,
            output.lower(),
            f"The output of your program is not correct. The values 100, 100 and 100 are not valid. The output of your program was: {output}",
        )

        mocked_input.side_effect = ["200", "-10", "-10"]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()

        expected_out = "not valid"
        self.assertIn(
            expected_out,
            output.lower(),
            f"The output of your program is not correct. The values 200, -10, -10 are not valid. The output of your program was: {output}",
        )


if __name__ == "__main__":
    unittest.main()
