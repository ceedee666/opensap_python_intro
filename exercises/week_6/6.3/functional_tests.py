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
    def test_output(self):

        self.code, self.std_out, self.error_out, _ = runcaptured()
        output = self.std_out.getvalue().strip().lower()

        self.assertIn(
            "mean", output, "The output of your program should contain the word Mean."
        )
        self.assertIn(
            "standard deviation",
            output,
            "The output of your program should contain the word Standard Deviations.",
        )

    def test_gaussian_distribution(self):
        with capture():
            import exercise as user

        result = user.gaussian_distribution()

        self.assertIsInstance(
            result, list, "The function gaussian_distribution() should return a list."
        )

        self.assertEqual(
            1000,
            len(result),
            "The function gaussian_distribution() should return a list with 1000 random values.",
        )

        self.assertTrue(
            any([result[0] != e for e in result]),
            "The function gaussian_distribution() should return a list with different values.",
        )

        self.assertGreaterEqual(
            len(set(result)),
            500,
            "The function gaussian_distribution() should return a list with different values.",
        )


if __name__ == "__main__":
    unittest.main()
