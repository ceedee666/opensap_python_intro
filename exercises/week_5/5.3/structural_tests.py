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

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id == "range":
                self.stats["range"] += 1

            if node.func.id == "is_even":
                self.stats["is_even"] += 1

            if node.func.id == "print":
                self.stats["print"] += 1
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.stats["function_def"] += 1
        if node.name == "is_even":
            self.stats["correct_function_name"] = True
            self.stats["function_args_count"] = len(node.args.args)
        self.generic_visit(node)

    def visit_For(self, node):
        self.stats["for"] += 1
        self.generic_visit(node)

    def visit_Return(self, node):
        self.stats["return"] += 1
        if isinstance(node.value, ast.Constant):
            if node.value.value == True:
                self.stats["return_true"] += 1
            if node.value.value == False:
                self.stats["return_false"] += 1
        self.generic_visit(node)


class Testing(TestCase):
    def test_function(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

        analyzer = Analyzer()
        analyzer.visit(tree)

        self.assertEqual(
            analyzer.stats["correct_function_name"],
            1,
            "You need to create one function named is_even() to solve this exercise.",
        )

        self.assertEqual(
            analyzer.stats["function_args_count"],
            1,
            "You need to create a function named is_even() with exactly one parameter to solve this exercise.",
        )

        self.assertGreaterEqual(
            analyzer.stats["return"],
            1,
            "You need to use at least one return statement to solve this exercise",
        )

    def test_function_call(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

        analyzer = Analyzer()
        analyzer.visit(tree)
        self.assertEqual(
            analyzer.stats["is_even"],
            1,
            "You need to call the is_even() function once to solve this exercise.",
        )

    def test_source_code(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertEqual(
                analyzer.stats["range"],
                1,
                "You need to use the range function one time to solve this exercise.",
            )

            self.assertEqual(
                analyzer.stats["print"],
                2,
                "You need to use the print function twice to solve this exercise.",
            )


if __name__ == "__main__":
    unittest.main()
