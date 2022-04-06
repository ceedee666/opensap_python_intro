import ast, unittest
from collections import defaultdict


class Analyzer(ast.NodeVisitor):
    """Analyzer class to parse & process ast"""

    def __init__(self):
        self.stats = defaultdict(int)

    def visit_withitem(self, node):
        # check if open() was used w/ with
        if (
            isinstance(node.context_expr, ast.Call)
            and node.context_expr.func.id == "open"
        ):
            self.stats["with_open"] += 1
        self.generic_visit(node)

    def visit_Call(self, node):
        # check if open() was used in read-mode or in write-mode
        for argument in node.args:
            if (
                isinstance(argument, ast.Constant)
                and node.func.id == "open"
                and argument.value == "r"
            ):
                self.stats["open_read"] += 1

            elif (
                isinstance(argument, ast.Constant)
                and node.func.id == "open"
                and argument.value == "w"
            ):
                self.stats["open_write"] += 1

        self.generic_visit(node)


class Testing(unittest.TestCase):
    """Testing class with multiple tests"""

    @classmethod
    def setUpClass(self):
        """Setup for just-once actions"""

        super().setUpClass()
        with open("exercise.py", "r") as source:
            self.code = source.read()

    def test_source_code(self):
        """Analyzer class to parse & process AST"""

        tree = ast.parse(self.code)  # build the AST
        analyzer = Analyzer()  # create Analyzer instance
        analyzer.visit(tree)  # visit the nodes of the AST

        used_with_open = analyzer.stats["with_open"]
        used_open_read = analyzer.stats["open_read"]
        used_open_write = analyzer.stats["open_write"]

        self.assertGreaterEqual(
            used_with_open,
            1,
            "You should always use a with statement when opening a file.",
        )

        self.assertEqual(
            2,
            used_open_read,
            "You need to open 2 files in read mode to get the input data.",
        )

        self.assertEqual(
            1,
            used_open_write,
            "You need to open an output file in write-mode to write your 'decrypted' data to.",
        )


if __name__ == "__main__":
    unittest.main()
