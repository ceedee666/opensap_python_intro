import ast
import unittest
from collections import defaultdict


class Analyzer(ast.NodeVisitor):
    """Analyzer class to parse & process ast"""

    def __init__(self):
        self.stats = defaultdict(int)

    def visit_withitem(self, node):
        # check if open() was used w/ with
        if isinstance(node.context_expr, ast.Call):
            if isinstance(node.context_expr.func, ast.Name):
                if node.context_expr.func.id == "open":
                    self.stats["with_open"] += 1

        self.generic_visit(node)

    def visit_Call(self, node):
        # check if open() was used in read-mode or in write-mode
        if isinstance(node.func, ast.Name):
            if node.func.id == "open":
                self.stats["open"] += 1

                for argument in node.args:
                    if isinstance(argument, ast.Constant):
                        if argument.value == "w":
                            self.stats["open_write"] += 1

        self.generic_visit(node)

    def visit_For(self, node):
        for sub_node in ast.walk(node):
            if isinstance(sub_node, ast.If):
                self.stats["for_if"] += 1
        self.generic_visit(node)

    def visit_While(self, node):
        for sub_node in ast.walk(node):
            if isinstance(sub_node, ast.While):
                self.stats["while_if"] += 1
        self.generic_visit(node)


class Testing(unittest.TestCase):
    """Testing class with multiple tests"""

    @classmethod
    def setUpClass(cls):
        """Setup for just-once actions"""

        super().setUpClass()
        with open("exercise.py", "r") as source:
            cls.code = source.read()

        tree = ast.parse(cls.code)  # build the AST
        cls.analyzer = Analyzer()  # create Analyzer instance
        cls.analyzer.visit(tree)  # visit the nodes of the AST

        cls.used_with_open = cls.analyzer.stats["with_open"]
        cls.used_open = cls.analyzer.stats["open"]
        cls.used_open_write = cls.analyzer.stats["open_write"]

    def test_file_io(self):

        self.assertGreaterEqual(
            self.used_with_open,
            1,
            "You should always use a with statement when opening a file.",
        )

        self.assertEqual(
            3,
            self.used_open,
            f"You need to open three files but you opened {self.used_open} file(s).",
        )

        self.assertEqual(
            1,
            self.used_open_write,
            f"You need to open one file in write mode to save the result, but you opened {self.used_open_write} file(s) in write mode.",
        )

    def test_for_while(self):
        if self.analyzer.stats["for_if"] < 1 and self.analyzer.stats["while_if"] < 1:
            self.fail(
                "You should use an if statement either in a for or in a while loop to compare the results."
            )


if __name__ == "__main__":
    unittest.main()
