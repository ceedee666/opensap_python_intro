exercise = __name__[1:]

import contextlib, io, sys, ast, os, unittest

from numpy import result_type
from test_exercise import stupid_function


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
        out[0] = out[0].getvalue()
        out[1] = out[1].getvalue()


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
    filename = "test_exercise.py"
    with open(filename) as f:
        source = f.read()
        c = compile(source, filename, "exec")
        with capture() as out, trace(tracing):
            if variables is None:
                variables = {}
            exec(c, variables)
        return source, out[0], out[1], variables


# here test w/ std_out, error_out
# possible to avoid terminal output of to-test-file? Or just don't care?
# TODO: How to not abort test/run when error in to-test-file??


class Testing(unittest.TestCase):

    # see https://docs.python.org/3/library/unittest.html#class-and-module-fixtures
    @classmethod
    def setUpClass(self):
        super().setUp()
        self.code, self.std_out, self.error_out, _ = runcaptured()
        # AST parsing and assign member variable

    def test_st_fct(self):
        a = 5
        b = 13
        result_test = a**b
        result_fct = stupid_function(a, b)
        self.assertEqual(result_test, result_fct)

    def test_output(self):
        expected_out = "Ditte is en Test\n"
        self.assertEqual(expected_out, self.std_out)


if __name__ == "__main__":
    unittest.main()
