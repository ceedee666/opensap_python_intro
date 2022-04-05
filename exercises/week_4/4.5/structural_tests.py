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
        # check if open() was used in read-mode
        for argument in node.args:
            if (
                isinstance(argument, ast.Constant)
                and node.func.id == "open"
                and argument.value == "r"
            ):
                self.stats["open_read"] += 1

        if isinstance(node.func, ast.Attribute) and node.func.attr == "split":
            self.stats["split"] += 1

        self.generic_visit(node)

    def visit_JoinedStr(self, node):
        self.stats["f_string"] += 1
        self.generic_visit(node)


class Testing(unittest.TestCase):
    """Testing class with multiple tests"""

    @classmethod
    def setUpClass(self):
        """Setup for just-once actions"""

        super().setUpClass()
        with open("reference.py", "r") as source:  # TODO: change
            self.code = source.read()

    def test_source_code(self):
        """Analyzer class to parse & process AST"""

        tree = ast.parse(self.code)  # build the AST
        analyzer = Analyzer()  # create Analyzer instance
        analyzer.visit(tree)  # visit the nodes of the AST

        used_with_open = analyzer.stats["with_open"]
        used_open_read = analyzer.stats["open_read"]
        used_split = analyzer.stats["split"]

        self.assertGreaterEqual(
            used_with_open,
            1,
            "You should always use a with statement when opening a file.",
        )

        self.assertEqual(
            1,
            used_open_read,
            "You need to open the file exactly one time in read mode to get the invoice data.",
        )

        self.assertEqual(
            1,
            used_split,
            f"You need to use the split() method to identify the individual parts of the lines once, but you used it {used_split} times.",
        )

        self.assertGreaterEqual(
            analyzer.stats["f_string"],
            1,
            "You should use an f-string so solve this exercise.",
        )


if __name__ == "__main__":
    unittest.main()
