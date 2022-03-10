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


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"print": 0, "input": 0, "vars": set()}

    def visit_Call(self, node):
        if node.func.id == "print":
            self.stats["print"] += 1

        if node.func.id == "input":
            self.stats["input"] += 1

        self.generic_visit(node)

    def visit_Assign(self, node):
        self.stats["vars"].add(node.targets[0].id)
        self.generic_visit(node)


class Testing(TestCase):
    @mock.patch("builtins.input", create=True)
    def test_output(self, mocked_input):
        mocked_input.side_effect = ["1", "1"]

        self.code, self.std_out, self.error_out, _ = runcaptured()
        expected_out = "The Phantom Menace"

        self.assertIn(
            expected_out,
            self.std_out.getvalue().strip(),
            "The output of your program is not correct. The expected output for the input 1 and 1 is: The Phantom Menace",
        )

        mocked_input.side_effect = ["3", "3"]

        self.code, self.std_out, self.error_out, _ = runcaptured()
        expected_out = "The Rise of Skywalker"

        self.assertIn(
            expected_out,
            self.std_out.getvalue().strip(),
            "The output of your program is not correct. The expected output for the input 3 and 3 is: The Rise of Skywalker",
        )
        mocked_input.side_effect = ["2", "2"]

        self.code, self.std_out, self.error_out, _ = runcaptured()
        expected_out = "The Empire Strikes Back"

        self.assertIn(
            expected_out,
            self.std_out.getvalue().strip(),
            "The output of your program is not correct. The expected output for the input 2 and 2 is: The Empire Strikes Back",
        )

    def test_source_code(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            if "star_wars_movies" not in analyzer.stats["vars"]:
                self.fail(
                    "You should define a variable named star_wars_movies.",
                )

            if analyzer.stats["print"] != 1:
                self.fail(
                    "You should use the print function one time.",
                )

            if analyzer.stats["input"] != 2:
                self.fail(
                    "You should use the input function two times.",
                )


if __name__ == "__main__":
    unittest.main()
