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
    def test_zero_production(self, mocked_input):
        mocked_input.side_effect = [600, 5, 10, 10, 10, 10, 10]

        self.code, self.std_out, self.error_out, _ = runcaptured()
        output = self.std_out.getvalue().strip().split("\n")

        self.assertEqual(
            len(output),
            6,
            f"For a planning of five month the output should contain six lines. Your output is: \n {self.std_out.getvalue().strip()}",
        )
        self.assertIn("The resulting production quantities are", output[0])
        self.assertIn(
            "0",
            output[1],
            f"For an initial stock of 600 and a sales plan of 10, 10, 10, 10, 10 the production quantity in the first month should be 0. Your output is:\n {output[1]}",
        )

        self.assertIn(
            "0",
            output[2],
            f"For an initial stock of 600 and a sales plan of 10, 10, 10, 10, 10 the production quantity in the second month should be 0. Your output is:\n {output[2]}",
        )
        self.assertIn(
            "0",
            output[3],
            f"For an initial stock of 600 and a sales plan of 10, 10, 10, 10, 10 the production quantity in the third month should be 0. Your output is:\n {output[3]}",
        )
        self.assertIn(
            "0",
            output[4],
            f"For an initial stock of 600 and a sales plan of 10, 10, 10, 10, 10 the production quantity in the fourth month should be 0. Your output is:\n {output[4]}",
        )
        self.assertIn(
            "0",
            output[5],
            f"For an initial stock of 600 and a sales plan of 10, 10, 10, 10, 10 the production quantity in the fifth month should be 0. Your output is:\n {output[5]}",
        )

    @mock.patch("builtins.input", create=True)
    def test_production(self, mocked_input):
        mocked_input.side_effect = [300, 4, 100, 400, 200, 10]

        self.code, self.std_out, self.error_out, _ = runcaptured()
        output = self.std_out.getvalue().strip().split("\n")

        self.assertEqual(
            len(output),
            5,
            f"For a planning of four month the output should contain five lines. Your output is: \n {self.std_out.getvalue().strip()}",
        )
        self.assertIn("The resulting production quantities are", output[0])
        self.assertIn(
            "0",
            output[1],
            f"For an initial stock of 300 and a sales plan of 100, 400, 200, 10 the production quantity in the first month should be 0. Your output is:\n {output[1]}",
        )

        self.assertIn(
            "0",
            output[2],
            f"For an initial stock of 300 and a sales plan of 100, 400, 200, 10 the production quantity in the second month should be 200. Your output is:\n {output[2]}",
        )
        self.assertIn(
            "0",
            output[3],
            f"For an initial stock of 300 and a sales plan of 100, 400, 200, 10 the production quantity in the third month should be 200. Your output is:\n {output[3]}",
        )
        self.assertIn(
            "0",
            output[4],
            f"For an initial stock of 300 and a sales plan of 100, 400, 200, 10 the production quantity in the fourth month should be 10. Your output is:\n {output[4]}",
        )


if __name__ == "__main__":
    unittest.main()
