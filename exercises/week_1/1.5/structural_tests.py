import ast
import os
import sys
import unittest
from unittest import TestCase

sys.modules["assess"] = sys.modules[__name__]
dirname = os.path.dirname(__file__)


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"input": 0, "int": 0, "print": 0, "vars": set()}

    def visit_Call(self, node):
        if node.func.id == "input":
            self.stats["input"] += 1
        if node.func.id == "int":
            self.stats["int"] += 1
        elif node.func.id == "print":
            self.stats["print"] += 1
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

            self.assertEqual(
                analyzer.stats["input"],
                3,
                f'You should use the input() function three times but you only used it {analyzer.stats["input"]} times.',
            )
            self.assertGreaterEqual(
                analyzer.stats["int"],
                3,
                f'You should use the int() function at least three times but you used it {analyzer.stats["int"]} times. The int() function is required to convert the input into an integer number.',
            )
            self.assertEqual(
                analyzer.stats["print"],
                1,
                "You should use the print() function one time.",
            )

            number_vars = len(analyzer.stats["vars"])
            self.assertGreaterEqual(
                number_vars,
                2,
                f"You should use at least two variables but you only used {number_vars} variables.",
            )
            self.assertLessEqual(
                number_vars,
                4,
                f"You should use not more than four variables but you used {number_vars} variables.",
            )


if __name__ == "__main__":
    unittest.main()
