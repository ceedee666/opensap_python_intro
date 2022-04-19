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
        if isinstance(node.func, ast.Attribute):
            if node.func.attr in ["get", "json"]:
                self.stats[node.func.attr] += 1
        self.generic_visit(node)

    def visit_Import(self, node):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "requests":
                    self.stats["import_requests"] += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.stats["for"] += 1
        self.generic_visit(node)


class Testing(TestCase):
    def test_import_requests(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertGreaterEqual(
                analyzer.stats["import_requests"],
                1,
                "You should import the requests library to solve this exercise.",
            )

    def test_for_loop(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertGreaterEqual(
                analyzer.stats["for"],
                1,
                "You should use a for loop to print the results returned by the search service.",
            )

    def test_methods(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertGreaterEqual(
                analyzer.stats["get"],
                1,
                "You should use the get method from the requests library to solve this exercise.",
            )
            self.assertGreaterEqual(
                analyzer.stats["json"],
                1,
                "You should use the json method from the requests library to solve this exercise.",
            )

    def test_in_and_output(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertGreaterEqual(
                analyzer.stats["input"],
                1,
                "You need to use the input function once to solve this exercise.",
            )

            self.assertGreaterEqual(
                analyzer.stats["print"],
                2,
                "You need to use the print function twice to solve this exercise.",
            )


if __name__ == "__main__":
    unittest.main()
