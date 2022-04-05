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


class Testing(TestCase):
    def test_function_reaction_path(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertEqual(
                analyzer.stats["reaction_path"],
                True,
                "You need to define a function reaction_path() to solve this exercise",
            )

            self.assertEqual(
                analyzer.stats["reaction_path_args_count"],
                1,
                "You need to define a function reaction_path() with one parameter to solve this exercise",
            )

    def test_function_brake_distance(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertEqual(
                analyzer.stats["brake_distance"],
                True,
                "You need to define a function brake_distance() to solve this exercise",
            )

            self.assertEqual(
                analyzer.stats["brake_distance_args_count"],
                1,
                "You need to define a function brake_distance() with one parameter to solve this exercise",
            )

    def test_function_stopping_distance(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertEqual(
                analyzer.stats["stopping_distance"],
                True,
                "You need to define a function stopping_distance() to solve this exercise",
            )

            self.assertEqual(
                analyzer.stats["stopping_distance_args_count"],
                1,
                "You need to define a function stopping_distance() with one parameter to solve this exercise",
            )


if __name__ == "__main__":
    unittest.main()
