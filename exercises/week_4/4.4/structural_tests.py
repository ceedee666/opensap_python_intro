import ast, unittest


class Analyzer(ast.NodeVisitor):
    """Analyzer class to parse & process ast"""

    def __init__(self):
        self.stats_if = []

    def visit_withitem(self, node):
        # check for with-open structure in source code
        for sub_node in ast.walk(node):
            if isinstance(sub_node, ast.Call) and sub_node.func.id == "open":
                for element in sub_node.args:
                    if (
                        isinstance(element, ast.Constant)
                        and element.value == "numbers.txt"
                    ):
                        # TODO: Find a less shitty way to check that
                        print("numbers.txt in open found")

    def visit_If(self, node):
        self.stats_if.append(node.lineno)
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

        used_ifs = len(analyzer.stats_if)

        self.assertGreaterEqual(
            1,
            used_ifs,
            "You did not use the correct number of if statements. "
            f"You need at least one if statement to check if a number is even, but you used {used_ifs}.",
        )


if __name__ == "__main__":
    unittest.main()
