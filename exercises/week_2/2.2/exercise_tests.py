import ast
import contextlib
import io
import os
import sys
import unittest
from unittest import TestCase

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
        self.stats = {"print": 0, "vars": set(), "list_dimensions": []}

    def visit_Call(self, node):
        if node.func.id == "print":
            self.stats["print"] += 1

            if len(node.args) == 1:
                if isinstance(node.args[0], ast.Subscript):
                    if node.args[0].value.value.id == "star_wars_movies":
                        self.stats["correct_var_in_print"] = True

        self.generic_visit(node)

    def visit_Assign(self, node):
        self.stats["vars"].add(node.targets[0].id)
        self.generic_visit(node)

    def visit_List(self, node):
        self.stats["list_dimensions"].append(len(node.elts))

        self.generic_visit(node)


class Testing(TestCase):
    def test_output(self):
        self.code, self.std_out, self.error_out, _ = runcaptured()
        expected_out = "Return of the Jedi"

        self.assertEqual(
            self.std_out.getvalue().strip(),
            expected_out,
            "The output of your program is not correct. The expected output is: Return of the Jedi",
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

            if analyzer.stats["list_dimensions"][0] != 3:
                self.fail(
                    "The variable star_wars_movies should contain a list of length 3.",
                )

            if not all([x == 3 for x in analyzer.stats["list_dimensions"][1:]]):
                self.fail(
                    "All elements of the list star_wars_movies should again be lists of length 3.",
                )

            if analyzer.stats["print"] != 1:
                self.fail(
                    "You should use the print function one time.",
                )

            if "correct_var_in_print" not in analyzer.stats:
                self.fail(
                    "You should use the variable star_wars_movies when calling the print function.",
                )


if __name__ == "__main__":
    unittest.main()
