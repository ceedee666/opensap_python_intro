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


class ReferenceImplementation:
    def is_prime(self, candidate):
        for i in range(2, candidate):
            if candidate % i == 0:
                return False
        return True

    def prime_list(self, max_number):
        list_primes = []
        for i in range(2, max_number + 1):
            if self.is_prime(i):
                list_primes.append(i)
        return list_primes


class Testing(TestCase):
    @mock.patch("builtins.input", create=True)
    def test_output(self, mocked_input):

        mocked_input.side_effect = ["10"]
        self.code, self.std_out, self.error_out, _ = runcaptured()
        output = self.std_out.getvalue().strip()

        primes = ["2", "3", "5", "7"]
        for prime in primes:
            self.assertIn(
                prime,
                output,
                f"The output of your program is not correct. For the input 10 the output should contain the number {prime}",
            )

    @mock.patch("builtins.input", create=True)
    def test_is_prime(self, mocked_input):
        mocked_input.side_effect = ["10"]
        with capture():
            import exercise as user

        for i in range(2, 1000):
            result = user.is_prime(i)
            expected_result = ReferenceImplementation().is_prime(i)

            self.assertEqual(
                expected_result,
                result,
                f"Your function is_prime() is not correct. For the number {i} is_prime should return {expected_result}. Your function returned {result}.",
            )

    @mock.patch("builtins.input", create=True)
    def test_prim_list(self, mocked_input):
        mocked_input.side_effect = ["10"]
        with capture():
            import exercise as user

        result = user.prime_list(1000)
        expected_result = ReferenceImplementation().prime_list(1000)

        self.assertIsInstance(
            result,
            list,
            "Your function prime_list() is not correct. The function should return a list.",
        )

        self.assertEqual(
            expected_result,
            result,
            f"Your function prime_list() is not correct. For the number 1000 the resultlist should contain the following number: {expected_result}",
        )


if __name__ == "__main__":
    unittest.main()
