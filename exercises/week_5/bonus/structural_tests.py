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
        self.stats[f"def_{node.name}"] = True
        self.stats[f"def_{node.name}_args_count"] = len(node.args.args)
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.stats[node.func.id] += 1
        self.generic_visit(node)


class Testing(TestCase):
    def test_function_is_prime(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertEqual(
                analyzer.stats["def_is_prime"],
                True,
                "You need to define a function is_prime() to solve this exercise.",
            )

            self.assertEqual(
                analyzer.stats["def_is_prime_args_count"],
                1,
                "You need to define a function is_prime() with one parameter to solve this exercise.",
            )

    def test_function_prime_list(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertEqual(
                analyzer.stats["def_prime_list"],
                True,
                "You need to define a function prime_list() to solve this exercise.",
            )

            self.assertEqual(
                analyzer.stats["def_prime_list_args_count"],
                1,
                "You need to define a function prime_list() with one parameter to solve this exercise.",
            )

    def test_in_and_output(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertGreaterEqual(
                analyzer.stats["int"],
                1,
                "You need to use the int() function at least once to solve this exercise.",
            )
            self.assertGreaterEqual(
                analyzer.stats["input"],
                1,
                "You need to use the input() function once to solve this exercise.",
            )

            self.assertGreaterEqual(
                analyzer.stats["print"],
                1,
                "You need to use the print() function once to solve this exercise.",
            )


if __name__ == "__main__":
    unittest.main()
