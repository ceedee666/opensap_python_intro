import contextlib, io, ast, unittest

from numpy import isin


@contextlib.contextmanager
def capture():
    """Helper function to get std(out&err)"""

    global captured_out
    import sys

    oldout, olderr = sys.stdout, sys.stderr
    try:
        out = [io.StringIO(), io.StringIO()]
        captured_out = out
        sys.stdout, sys.stderr = out
        yield out
    finally:
        sys.stdout, sys.stderr = oldout, olderr
        out[0] = out[0].getvalue()
        out[1] = out[1].getvalue()


@contextlib.contextmanager
def trace(t):
    try:
        if t:
            t.start()
        yield
    finally:
        if t:
            t.stop()


def runcaptured(filename, tracing=None, variables=None):
    """Run a specified python file and return source code, stdout, stderr and variables"""

    with open(filename) as f:
        source = f.read()
        c = compile(source, filename, "exec")
        with capture() as out, trace(tracing):
            if variables is None:
                variables = {}
            exec(c, variables)
        return source, out[0], out[1], variables


class Analyzer(ast.NodeVisitor):
    """Analyzer class to parse & process ast"""

    def __init__(self):
        self.stats = {"open": 0, "strip": 0, "int": 0}

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


class Testing(unittest.TestCase):
    """Testing class with multiple tests"""

    @classmethod
    def setUpClass(self):
        """Setup for just-once actions"""

        super().setUpClass()
        self.code, self.std_out, self.error_out, _ = runcaptured("exercise.py")

    def test_source_code(self):
        """Analyzer class to parse & process AST"""

        tree = ast.parse(self.code)  # build the AST
        analyzer = Analyzer()  # create Analyzer instance
        analyzer.visit(tree)  # visit the nodes of the AST

        used_opens = analyzer.stats["open"]
        used_strips = analyzer.stats["strip"]
        used_ints = analyzer.stats["int"]

        self.assertEqual(
            1,
            used_opens,
            "You did not use the corrent number of open() statements. "
            f"You need to use 1 open() statement to read the input file, but you used {used_opens}.",
        )

        self.assertEqual(
            1,
            used_strips,
            "You did not use the corrent number of strip() statements. "
            f"You just need to remove the line breaks from your input lines. You used {used_strips} strip() statements.",
        )

        self.assertEqual(
            1,
            used_ints,
            "You did not use the corrent number of type cast statements. "
            f"You need to convert the input from your file into integer numbers. You used {used_ints} int() statements",
        )


if __name__ == "__main__":
    unittest.main()
