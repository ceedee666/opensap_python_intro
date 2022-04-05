import ast, unittest


class Analyzer(ast.NodeVisitor):
    """Analyzer class to parse & process ast"""

    def __init__(self):
        self.stats = {"XXXX": 0, "YYYY": 0, "ZZZZ": 0}

    def visit_Call(self, node):
        for sub_node in ast.walk(node):
            if isinstance(sub_node, ast.Name) and sub_node.id == "XXXX":
                self.stats["XXXX"] += 1

            if isinstance(sub_node, ast.Attribute) and sub_node.attr == "YYYY":
                self.stats["YYYY"] += 1
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node, ast.Name) and node.id == "ZZZZ":
            self.stats["ZZZZ"] += 1
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

        used_XXXX = analyzer.stats["open"]

        self.assertEqual(
            1,
            used_XXXX,
            "You did not use the correct number of XXXX statements. "
            f"WHATEVER, but you used {used_XXXX}.",
        )


if __name__ == "__main__":
    unittest.main()
