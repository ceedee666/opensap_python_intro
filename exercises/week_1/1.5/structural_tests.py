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
        self.stats = {"input": 0, "int": 0, "print": 0, "vars": set()}

    def visit_Call(self, node):
        if node.func.id == "input":
            self.stats["input"] += 1
        if node.func.id == "int":
            self.stats["int"] += 1
        elif node.func.id == "print":
            self.stats["print"] += 1
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

            self.assertEqual(
                analyzer.stats["input"],
                3,
                f'You should use the input function three times but you only used it {analyzer.stats["input"]} times.',
            )
            self.assertEqual(
                analyzer.stats["int"],
                3,
                f'You should use the int function three times but you only used it {analyzer.stats["input"]} times. The int function is required to convert the input into an integer number.',
            )
            self.assertEqual(
                analyzer.stats["print"],
                1,
                "You should use the print function one time.",
            )

            number_vars = len(analyzer.stats["vars"])
            self.assertGreaterEqual(
                number_vars,
                3,
                f"You should use at least three variables but you only used {number_vars} variables.",
            )
            self.assertLessEqual(
                number_vars,
                4,
                f"You should use not more than four variables but you used {number_vars} variables.",
            )


if __name__ == "__main__":
    unittest.main()
