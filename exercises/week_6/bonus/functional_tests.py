import contextlib
import io
import math
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
        lines = output.split("\n")

        self.assertEqual(
            3, len(lines), "The output of your program should consist of three lines."
        )
        self.assertIn(
            "3.1",
            lines[0],
            "The first output line should contain the calculated value of π stating with 3",
        )

        self.assertIn(
            str(math.pi),
            lines[1],
            "The second line should contain the value of π from the math library",
        )


if __name__ == "__main__":
    unittest.main()
