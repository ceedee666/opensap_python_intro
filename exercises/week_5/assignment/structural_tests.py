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

    def visit_FunctionDef(self, node):
        self.stats[node.name] = True
        self.stats[f"{node.name}_args_count"] = len(node.args.args)
        self.generic_visit(node)

    def visit_call(self, node):
        if isinstance(node.func, ast.Name):
            self.stats[node.func.id] += 1


class Testing(TestCase):
    def test_function_encrypt_letter(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertEqual(
                analyzer.stats["encrypt_letter"],
                True,
                "You need to define a function encrypt_letter() to solve this exercise.",
            )

            self.assertEqual(
                analyzer.stats["encrypt_letter_args_count"],
                2,
                "You need to define a function encrypt_letter() with two parameter to solve this exercise.",
            )

    def test_function_calculate_shifts(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertEqual(
                analyzer.stats["calculate_shifts"],
                True,
                "You need to define a function calculate_shifts() to solve this exercise.",
            )

            self.assertEqual(
                analyzer.stats["calculate_shifts_args_count"],
                1,
                "You need to define a function calculate_shifts() with one parameter to solve this exercise.",
            )

    def test_function_stopping_distance(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertEqual(
                analyzer.stats["encrypt_text"],
                True,
                "You need to define a function encrypt_text() to solve this exercise.",
            )

            self.assertEqual(
                analyzer.stats["encrypt_text_args_count"],
                2,
                "You need to define a function encrypt_text() with one parameter to solve this exercise.",
            )

    def test_in_and_output(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertGreaterEqual(
                analyzer.stats["input"],
                2,
                "You need to use the input function two times to solve this exercise.",
            )

            self.assertGreaterEqual(
                analyzer.stats["print"],
                1,
                "You need to use the print function one time to solve this exercise.",
            )


if __name__ == "__main__":
    unittest.main()
