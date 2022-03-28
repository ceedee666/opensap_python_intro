import ast
import os
import sys
import unittest
from unittest import TestCase

sys.modules["assess"] = sys.modules[__name__]
dirname = os.path.dirname(__file__)


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"tuple": 0}
        self.nested_for = False

    def visit_Tuple(self, node):
        self.stats["tuple"] += 1

        self.generic_visit(node)


class Testing(TestCase):
    def test_source_code(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertGreaterEqual(
                analyzer.stats["tuple"],
                1,
                "You need to create a tuple to solve this exercise.",
            )


if __name__ == "__main__":
    unittest.main()
