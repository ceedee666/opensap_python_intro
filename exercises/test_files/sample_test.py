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
    """Sample Analyzer class to parse & process AST"""

    def __init__(self):
        self.stats = []                     # create empty stats list


    def visit_If(self, node):               # list number of ifs in test file
        self.stats.append(node.lineno)      # append line occurrences of ifs
        self.generic_visit(node)
        self.num_ifs = len(self.stats)      # return no of ifs


    def report(self):
        print(self.stats)



class Testing(unittest.TestCase):
    """Sample Testing class with multiple tests"""


    @classmethod
    def setUpClass(self):
        """Setup for just-once actions"""

        super().setUpClass()
        self.code, self.std_out, self.error_out, _ = runcaptured("sample_exercise.py")


    def test_ast_parse(self):
        tree = ast.parse(self.code)                         # build the AST
        analyzer = Analyzer()                               # create Analyzer instance
        analyzer.visit(tree)                                # visit the nodes of the AST
        analyzer.report()                                   # report result(s)

        # test number of ifs
        expected_ifs = 3
        self.assertEqual(expected_ifs, analyzer.num_ifs,
            f"You did not use the demanded number of ifs (3), you used if clauses in lines: {analyzer.stats}")


    def test_st_fct(self):
        from sample_exercise import stupid_function         # import function only where needed/tested

        a = 5
        b = 13
        expected_result = a**b
        fct_result = stupid_function(a, b)

        self.assertEqual(expected_result, fct_result, "Your function did not return the expected result.")


    def test_output(self):
        expected_out = "Ditte is en Test\n"
        self.assertEqual(expected_out, self.std_out, "The output of your function did not generate the expected output")


if __name__ == "__main__":
    unittest.main()
