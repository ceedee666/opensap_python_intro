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

    def visit_Import(self, node):
        for n in node.names:
            if n.name == "random":
                self.stats["import_random"] = True
            if n.name == "statistics":
                self.stats["import_statistics"] = True
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module == "random":
            self.stats["import_random"] = True
        if node.module == "statistics":
            self.stats["import_statistics"] = True
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.stats[node.func.id] += 1
        if isinstance(node.func, ast.Attribute):
            self.stats[node.func.attr] += 1
        self.generic_visit(node)


class Testing(TestCase):
    def test_function_gaussian_distribution(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertEqual(
                analyzer.stats["def_gaussian_distribution"],
                True,
                "You need to define a function gaussian_distribution() to solve this exercise.",
            )

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
                analyzer.stats["gauss"],
                1,
                "You need to use the gauss() function at least once to solve this exercise.",
            )

    def test_stat_module(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertTrue(
                analyzer.stats["import_statistics"],
                "You need to import the statistics module to solve this exercise",
            )
            self.assertGreaterEqual(
                analyzer.stats["mean"],
                1,
                "You need to use the mean() function at least once to solve this exercise.",
            )
            self.assertGreaterEqual(
                analyzer.stats["stdev"],
                1,
                "You need to use the stdev() function at least once to solve this exercise.",
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
            self.assertGreaterEqual(
                analyzer.stats["print"],
                1,
                "You need to use the print() function at least once to solve this exercise.",
            )


if __name__ == "__main__":
    unittest.main()
