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
    def test_output(self):
        self.code, self.std_out, self.error_out, _ = runcaptured()

        output = self.std_out.getvalue().strip()
        if (
            (not "TSLA" in output)
            or (not "ZM" in output)
            or ("SAP" in output)
            or ("APPL" in output)
            or ("ORCL" in output)
        ):
            self.fail("The output should only contain the stock symbols TSLA and ZM")


if __name__ == "__main__":
    unittest.main()
