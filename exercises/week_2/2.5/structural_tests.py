import ast
import os
import sys
import unittest
from unittest import TestCase

sys.modules["assess"] = sys.modules[__name__]
dirname = os.path.dirname(__file__)


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

        self.generic_visit(node)

    def visit_For(self, node):
        self.stats["for"] += 1

        for element in node.body:
            if isinstance(element, ast.For):
                self.nested_for = True

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

            self.assertGreaterEqual(
                analyzer.stats["input"],
                3,
                "You need to use three calls to the input() function to solve this exercise.",
            )

            self.assertGreaterEqual(
                analyzer.stats["int"],
                3,
                "You need to use three calls to the int() function to convert to user input to type integer.",
            )

            self.assertGreaterEqual(
                analyzer.stats["append"],
                1,
                "You should use the append() method to add the user input to the matrix.",
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
