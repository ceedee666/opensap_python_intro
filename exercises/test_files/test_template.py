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
    # possible to avoid terminal output of to-test-file when running? Or just don't care?

    with open(filename) as f:
        source = f.read()
        c = compile(source, filename, "exec")
        with capture() as out, trace(tracing):
            if variables is None:
                variables = {}
            exec(c, variables)
        return source, out[0], out[1], variables


####################################
# Adapt tests & AST beginning here #
####################################
class Analyzer(ast.NodeVisitor):
    """Sample Analyzer class to parse & process ast"""

    def __init__(self):
        self.stats = []                     # create empty stats list


    def visit_If(self, node):
        # adaption here
        self.generic_visit(node)


    def visit_For(self, node):
        # adaption here
        self.generic_visit(node)



class Testing(unittest.TestCase):
    """Sample Testing class with multiple tests"""

    @classmethod
    def setUpClass(self):
        """Setup for just-once actions"""

        super().setUpClass()
        self.code, self.std_out, self.error_out, _ = runcaptured("exercise_name.py")    # change filename accordingly


    def test_ast_parse(self):
        """Sample Analyzer class to parse & process AST"""

        tree = ast.parse(self.code)                         # build the AST
        analyzer = Analyzer()                               # create Analyzer instance
        analyzer.visit(tree)                                # visit the nodes of the AST
        analyzer.report()                                   # report result(s)

        # test number of ifs
        expected_ifs = 3
        self.assertEqual(expected_ifs, analyzer.num_ifs, "#CHANGE# - error return message")


    def test_st_fct(self):
        from template_exercise import template_function         # import function only where needed/tested

        a = 5
        b = 13
        expected_result = a**b
        fct_result = template_function(a, b)

        self.assertEqual(expected_result, fct_result, "#CHANGE# - error return message")


    def test_output(self):
        expected_out = "Ditte is en Test\n"
        self.assertEqual(expected_out, self.std_out, "#CHANGE# - error return message")


if __name__ == "__main__":
    unittest.main()
