# Proposed tests
#
# - check if function `reaction_path()` is available
# - check if function `brake_distance()` is available
# - check if function `stopping_distance()` is available
# - check if function `stopping_disctance()` calls the other two functions
# - check certain input values

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
    def test_reaction_path(self, mocked_input):
        mocked_input.side_effect = [50]
        with capture() as out:
            import exercise as user

        result = user.reaction_path(20)
        expected_out = 6.0
        self.assertEqual(
            expected_out,
            result,
            "The result of the function reaction_path is not correct.",
        )
        result = user.reaction_path(50)
        expected_out = 15.0
        self.assertEqual(
            expected_out,
            result,
            "The result of the function reaction_path is not correct.",
        )

    @mock.patch("builtins.input", create=True)
    def test_brake_distance(self, mocked_input):
        mocked_input.side_effect = [50]
        with capture() as out:
            import exercise as user

        result = user.brake_distance(20)
        expected_out = 4.0
        self.assertEqual(
            expected_out,
            result,
            "The result of the function brake_distance is not correct.",
        )
        result = user.brake_distance(50)
        expected_out = 25.0
        self.assertEqual(
            expected_out,
            result,
            "The result of the function brake_distance is not correct.",
        )

    @mock.patch("builtins.input", create=True)
    def test_stopping_distance(self, mocked_input):
        mocked_input.side_effect = [50]
        with capture() as out:
            import exercise as user

        result = user.stopping_distance(20)
        expected_out = 10.0
        self.assertEqual(
            expected_out,
            result,
            "The result of the function stopping_distance is not correct.",
        )
        result = user.stopping_distance(50)
        expected_out = 40.0
        self.assertEqual(
            expected_out,
            result,
            "The result of the function stopping_distance is not correct.",
        )

    @mock.patch("builtins.input", create=True)
    def test_program_result(self, mocked_input):
        mocked_input.side_effect = [50]

        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()

        expected_out = "40.0"
        self.assertIn(
            expected_out,
            output,
            "The output of your program is not correct. For a speed of 50 km/h the result should be 40.0.",
        )


if __name__ == "__main__":
    unittest.main()
