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
        self.stats = {"print": 0, "vars": set(), "for": 0, "append": 0}

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id == "print":
                self.stats["print"] += 1

                if len(node.args) == 1:
                    if isinstance(node.args[0], ast.Name):
                        if node.args[0].id == "sell_list":
                            self.stats["print_with_var"] = True

        if isinstance(node.func, ast.Attribute):
            if node.func.attr == "append":
                self.stats["append"] += 1
                if node.func.value.id == "sell_list":
                    self.stats["append_to_sell_list"] = True

        self.generic_visit(node)

    def visit_For(self, node):
        self.stats["for"] += 1

        if node.target.id == "stocks":
            self.stats["iterate_stocks"] = True

        self.generic_visit(node)

    def visit_Assign(self, node):
        self.stats["vars"].add(node.targets[0].id)
        self.generic_visit(node)


class Testing(TestCase):
    def test_source_code(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            if analyzer.stats["print"] != 1:
                self.fail(
                    "You should use the print function one time to print the sell_list."
                )

            if analyzer.stats["for"] != 1:
                self.fail(
                    "You should use one for loop to iterate through the list in the variable stocks."
                )
            if "stocks" not in analyzer.stats["vars"]:
                self.fail(
                    "You should define a variable named stock. This variable should contain the list given in the exercise.",
                )

            if "sell_list" not in analyzer.stats["vars"]:
                self.fail(
                    "You should define a variable named sell_list. This variable should contain a list of stock symbols to sell.",
                )

            if "print_with_var" not in analyzer.stats:
                self.fail(
                    "You should use the variable sell_list when calling the print function.",
                )

            if "append_to_sell_list" not in analyzer.stats:
                self.fail(
                    "You should use one append to add the stock symbols to the sell_list."
                )


if __name__ == "__main__":
    unittest.main()
