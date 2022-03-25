import contextlib, io, ast, unittest


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
    """Sample Analyzer class to parse & process ast"""

    def __init__(self):
        self.stats_print = []  # create empty stats list

    def visit_Call(self, node):
        if node.func.id == "print":
            self.stats_print.append(node.func.lineno)
        self.generic_visit(node)


class Testing(unittest.TestCase):
    """Sample Testing class to check code structure"""

    @classmethod
    def setUpClass(self):
        """Setup for just-once actions"""

        super().setUpClass()
        self.code, self.std_out, self.error_out, _ = runcaptured("exercise.py")

    def test_ast_parse(self):
        """Sample Analyzer class to parse & process AST"""

        tree = ast.parse(self.code)  # build the AST
        analyzer = Analyzer()  # create Analyzer instance
        analyzer.visit(tree)  # visit the nodes of the AST

        used_prints = len(analyzer.stats_print)

        self.assertEqual(
            1,
            used_prints,
            f"You did not use the correct number of print statements. "
            f"You should use just one print statement, but you used {used_prints}.",
        )


if __name__ == "__main__":
    unittest.main()
