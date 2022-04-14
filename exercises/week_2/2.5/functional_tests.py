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
        mocked_input.side_effect = [3, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip().split("\n")

        start_index = 0
        if len(output) == 4 and "matrix values" in output[0].lower():
            start_index = 1

        expected_out = "6"
        self.assertIn(
            expected_out,
            output[start_index],
            "The output of your program is not correct. The sum of the rows is not calculated correctly.",
        )

        expected_out = "15"
        self.assertIn(
            expected_out,
            output[start_index + 1],
            "The output of your program is not correct. The sum of the rows is not calculated correctly.",
        )

        expected_out = "24"
        self.assertIn(
            expected_out,
            output[start_index + 2],
            "The output of your program is not correct. The sum of the rows is not calculated correctly.",
        )

        for line in output[start_index:]:
            expected_out = "Sum of row"
            self.assertIn(
                expected_out,
                line,
                'The output of your program is not correct. Each line in the output should start with "Sum of row".',
            )


if __name__ == "__main__":
    unittest.main()
