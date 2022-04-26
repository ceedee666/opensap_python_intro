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
            if node.func.id == "input":
                self.stats["input"] += 1

            if node.func.id == "get_student_data":
                self.stats["get_student_data"] += 1

            if node.func.id == "print":
                self.stats["print"] += 1
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.stats["functions"] += 1

        self.generic_visit(node)

    def visit_Tuple(self, node):
        self.stats["tuple"] += 1
        self.generic_visit(node)


class Testing(TestCase):
    def test_function(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

        analyzer = Analyzer()
        analyzer.visit(tree)

        self.assertEqual(
            analyzer.stats["functions"],
            1,
            "You need to create one function named get_student_data() to solve this exercise.",
        )

        self.assertEqual(
            analyzer.stats["get_student_data"],
            1,
            "You need to call the get_student_data() function once to solve this exercise.",
        )

    def test_source_code(self):
        with open("exercise.py", "r") as source:
            tree = ast.parse(source.read())

            analyzer = Analyzer()
            analyzer.visit(tree)

            self.assertEqual(
                analyzer.stats["input"],
                3,
                "You need to use the input() function three times to solve this exercise.",
            )

            self.assertEqual(
                analyzer.stats["print"],
                1,
                "You need to use the print() function once to solve this exercise.",
            )

            self.assertEqual(
                analyzer.stats["tuple"],
                1,
                "You need create a tuple with the student data to solve this exercise.",
            )


if __name__ == "__main__":
    unittest.main()
