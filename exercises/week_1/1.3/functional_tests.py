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
    def test_output(self, mocked_input):
        mocked_input.side_effect = ["Christian", "Aachen", "Berlin", "Car"]

        self.code, self.std_out, self.error_out, _ = runcaptured()
        expected_out = "Christian wants to travel from Aachen to Berlin by Car"
        self.assertEqual(self.std_out.getvalue().strip(), expected_out)


if __name__ == "__main__":
    unittest.main()
