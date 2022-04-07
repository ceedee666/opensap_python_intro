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

    def visit_Attribute(self, node):
        if node.attr == "pi":
            self.stats["pi"] += 1

    def visit_Import(self, node):
        for n in node.names:
            if n.name == "random":
                self.stats["import_random"] = True
            if n.name == "math":
                self.stats["import_math"] = True
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module == "random":
            self.stats["import_random"] = True
        if node.module == "math":
            self.stats["import_statistics"] = True
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.stats[node.func.id] += 1
        if isinstance(node.func, ast.Attribute):
            self.stats[node.func.attr] += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.stats["for"] += 1

        self.generic_visit(node)


class Testing(TestCase):
    def test_random_module(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)
            self.assertTrue(
                analyzer.stats["import_random"],
                "You need to import the random module to solve this exercise",
            )

            self.assertGreaterEqual(
                analyzer.stats["random"],
                2,
                "You need to use the random() function at least once to solve this exercise.",
            )

    def test_math_modul(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertTrue(
                analyzer.stats["import_math"],
                "You need to import the math module to solve this exercise",
            )
            self.assertGreaterEqual(
                analyzer.stats["pi"],
                2,
                "You need to use the pi constant form the math module at least twice to solve this exercise.",
            )

    def test_standard_lib(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertGreaterEqual(
                analyzer.stats["range"],
                1,
                "You need to use the range() function at least once to solve this exercise.",
            )


if __name__ == "__main__":
    unittest.main()
