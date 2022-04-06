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
    def setUpClass(self):
        """Setup for just-once actions"""

        super().setUpClass()
        with open("reference.py", "r") as source:  # TODO. CHANGE##############
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
            f"You need to open two files in read mode to get the input data, but you opened {used_open_read} file(s).",
        )

        self.assertEqual(
            1,
            used_open_write,
            f"You need to open one file in write mode for the result, but you opened {used_open_write} file(s)",
        )

        if analyzer.stats["for_if"] < 1 and analyzer.stats["while_if"] < 1:
            self.fail(
                "You should use an if statement either in a for or in a while loop to compare the results."
            )


if __name__ == "__main__":
    unittest.main()
