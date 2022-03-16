import ast
import os
import sys
import unittest
from unittest import TestCase

sys.modules["assess"] = sys.modules[__name__]
dirname = os.path.dirname(__file__)


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"range": 0, "mod": 0, "other_ints": False}

    def visit_Constant(self, node):
        if isinstance(node.value, int):
            if node.value not in [0, 3, 5, 1, 100, 101]:
                self.stats["other_ints"] = True
        self.generic_visit(node)

    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Mod):
            self.stats["mod"] += 1

        self.generic_visit(node)

    def visit_Call(self, node):
        if node.func.id == "range":
            self.stats["range"] += 1
        self.generic_visit(node)


class Testing(TestCase):
    def setUp(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            self.analyzer = Analyzer()
            self.analyzer.visit(tree)

    def test_constant(self):
        self.assertFalse
        (
            self.analyzer.stats["other_ints"],
            "You should not use any other integers except 0, 1, 3, 5, 100 and 101 in your solutions. You do not need to use all of these!",
        )

    def test_mod(self):
        self.assertGreaterEqual
        (
            self.analyzer.stats["mod"],
            2,
            f"You should use the modulo operator (%) to check divisibility by 3 and 5.",
        )

    def test_range(self):
        self.assertGreaterEqual
        (
            self.analyzer.stats["range"],
            1,
            f"You should use the range function to create a list of number from 1 to 100.",
        )


if __name__ == "__main__":
    unittest.main()
