import ast
import os
import sys
import unittest
from collections import defaultdict
from unittest import TestCase

sys.modules["assess"] = sys.modules[__name__]
dirname = os.path.dirname(__file__)


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = defaultdict(int)
        self.nested_for = False

    def visit_Import(self, node):
        for n in node.names:
            if n.name == "sudoku":
                self.stats["import_sudoku"] = True
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module == "sudoku":
            self.stats["import_sudoku"] = True
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.stats[node.func.id] += 1
        if isinstance(node.func, ast.Attribute):
            self.stats[node.func.attr] += 1
        self.generic_visit(node)


class Testing(TestCase):
    def test_import_module(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)
            self.assertTrue(
                analyzer.stats["import_sudoku"],
                "You need to import the sudoku module to solve this exercise",
            )

    def test_function_calls(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertGreaterEqual(
                analyzer.stats["difficulty"],
                1,
                "You need to use the difficulty() function at least once to solve this exercise.",
            )

            self.assertGreaterEqual(
                analyzer.stats["show"],
                1,
                "You need to use the show() function at least once to solve this exercise.",
            )

            self.assertGreaterEqual(
                analyzer.stats["solve"],
                1,
                "You need to use the solve() function at least once to solve this exercise.",
            )


if __name__ == "__main__":
    unittest.main()
