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
        self.stats = {"input": 0, "vars": set(), "for": 0, "int": 0, "append": 0}
        self.nested_for = False

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id == "input":
                self.stats["input"] += 1

            if node.func.id == "int":
                self.stats["int"] += 1

        if isinstance(node.func, ast.Attribute):
            if node.func.attr == "append":
                self.stats["append"] += 1

    def visit_For(self, node):
        self.stats["for"] += 1

        for element in node.body:
            if isinstance(element, ast.For):
                self.nested_for == True

        self.generic_visit(node)

    def visit_Assign(self, node):
        self.stats["vars"].add(node.targets[0].id)
        self.generic_visit(node)


class Testing(TestCase):
    @mock.patch("builtins.input", create=True)
    def test_output(self, mocked_input):
        mocked_input.side_effect = [3, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip().split("\n")

        expected_out = "6"
        self.assertIn(
            expected_out,
            output[1],
            "The output of your program is not correct. The sum of the rows is not calculated correctly.",
        )

        expected_out = "15"
        self.assertIn(
            expected_out,
            output[2],
            "The output of your program is not correct. The sum of the rows is not calculated correctly.",
        )

        expected_out = "24"
        self.assertIn(
            expected_out,
            output[3],
            "The output of your program is not correct. The sum of the rows is not calculated correctly.",
        )

        for line in output[1:]:
            expected_out = "Sum of row"
            self.assertIn(
                expected_out,
                line,
                'The output of your program is not correct. Each line in the output should start with "Sum of row".',
            )

    def test_source_code(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertEqual(
                2,
                analyzer.stats["input"],
                "You need to use two calls to the input function to solve this exercise.",
            )

            self.assertEqual(
                2,
                analyzer.stats["int"],
                "You need to use two calls to the int function to convert to user input to type integer.",
            )

            self.assertGreaterEqual(
                1,
                analyzer.stats["append"],
                "You should use the append method to add the user input to the matrix.",
            )

    def test_nested_for(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            if not analyzer.nested_for:
                self.fail("You should use nested for loops to solve this exercise.")


if __name__ == "__main__":
    unittest.main()
