import ast
import os
import sys
import unittest
from unittest import TestCase

sys.modules["assess"] = sys.modules[__name__]
dirname = os.path.dirname(__file__)


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"input": 0, "lower": 0, "for": 0}
        self.nested_for = False

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id == "input":
                self.stats["input"] += 1

        if isinstance(node.func, ast.Attribute):
            if node.func.attr == "lower":
                self.stats["lower"] += 1

        self.generic_visit(node)

    def visit_For(self, node):
        self.stats["for"] += 1

        for element in node.body:
            if isinstance(element, ast.For):
                self.nested_for = True

        self.generic_visit(node)


class Testing(TestCase):
    def test_source_code(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertGreaterEqual(
                analyzer.stats["input"],
                1,
                "You need to use one call to the input function to get the plain text from the user.",
            )

            self.assertGreaterEqual(
                analyzer.stats["for"],
                1,
                "Youd should use a for loop to iterates through the letters of the user input.",
            )

    def test_functions(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertGreaterEqual(
                analyzer.stats["input"],
                1,
                "You need to use one call to the input function to get the plain text from the user.",
            )

            self.assertGreaterEqual(
                analyzer.stats["lower"],
                1,
                "You should use the lower method to convert the user input to lower case.",
            )

            self.assertGreaterEqual(
                analyzer.stats["for"],
                1,
                "Youd should use a for loop to iterates through the letters of the user input.",
            )


if __name__ == "__main__":
    unittest.main()
