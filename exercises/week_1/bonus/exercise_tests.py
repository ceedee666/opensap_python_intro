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
    def test_two_real_solutions(self, mocked_input):
        mocked_input.side_effect = ["4", "2", "-2"]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        out = self.std_out.getvalue().strip()

        if (
            "2 real solutions" not in out.lower()
            and "two real solutions" not in out.lower()
        ):
            self.fail(
                f"For the input 4, 2 and -2 the quadratic equation has 2 real solutions. The output of your program was {out}."
            )

    @mock.patch("builtins.input", create=True)
    def test_one_real_solutions(self, mocked_input):
        mocked_input.side_effect = ["4", "4", "1"]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        out = self.std_out.getvalue().strip()

        if (
            "1 real solution" not in out.lower()
            and "one real solution" not in out.lower()
        ):
            self.fail(
                f"For the input 4, 4 and 1 the quadratic equation has 1 real solution. The output of your program was {out}."
            )

    @mock.patch("builtins.input", create=True)
    def test_complex_solution(self, mocked_input):
        mocked_input.side_effect = ["4", "1", "2"]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        out = self.std_out.getvalue().strip()

        if (
            "2 complex solutions" not in out.lower()
            and "two complex solutions" not in out.lower()
        ):
            self.fail(
                f"For the input 4, 1 and 2 the quadratic equation has 2 complex solution. The output of your program was {out}."
            )


if __name__ == "__main__":
    unittest.main()
