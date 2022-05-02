import ast, unittest


class Analyzer(ast.NodeVisitor):
    """Analyzer class to parse & process ast"""

    def __init__(self):
        self.stats = {"open": 0, "strip": 0, "int": 0, "cheat": 0}

    def visit_Call(self, node):
        for sub_node in ast.walk(node):
            if isinstance(sub_node, ast.Name) and sub_node.id == "open":
                self.stats["open"] += 1

            if isinstance(sub_node, ast.Attribute) and sub_node.attr == "strip":
                self.stats["strip"] += 1
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node, ast.Name) and node.id == "int":
            self.stats["int"] += 1
        self.generic_visit(node)

    def visit_Constant(self, node):
        if node.value == 9853 or node.value == 9760 or node.value == 9745:
            self.stats["cheat"] += 1
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

        used_opens = analyzer.stats["open"]
        used_strips = analyzer.stats["strip"]
        used_ints = analyzer.stats["int"]
        cheats = analyzer.stats["cheat"]

        self.assertLessEqual(
            cheats,
            0,
            "Please do not use hardcoded solutions. Anybody could do that... ;-)",
        )

        self.assertEqual(
            1,
            used_opens,
            "You did not use the correct number of open() statements. "
            f"You need to use 1 open() statement to read the input file, but you used {used_opens}.",
        )

        self.assertEqual(
            1,
            used_strips,
            "You did not use the correct number of strip() statements. "
            f"You just need to remove the line breaks from your input lines. You used {used_strips} strip() statements.",
        )

        self.assertEqual(
            1,
            used_ints,
            "You did not use the correct number of type cast statements. "
            f"You need to convert the input from your file into integer numbers. You used {used_ints} int() statements",
        )


if __name__ == "__main__":
    unittest.main()
