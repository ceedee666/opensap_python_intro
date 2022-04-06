import contextlib, io, unittest


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


class Testing(unittest.TestCase):
    """Testing class with multiple tests"""

    @classmethod
    def setUpClass(self):
        """Setup for just-once actions"""

        super().setUpClass()
        self.code, self.std_out, self.error_out, _ = runcaptured("exercise.py")

    def test_output_file(self):
        """Test if expected output file exists and compare with reference file"""

        with open("result_reference.txt", "r") as reference:
            reference_file_out = reference.read()

        try:
            with open("result.txt", "r") as input_file:
                self.assertEqual(
                    reference_file_out,
                    input_file.read(),
                    "The content of your output file is not correct.",
                )
        except FileNotFoundError:
            self.fail(
                "The expected file 'result.txt' was not found. Did you create it?"
            )


if __name__ == "__main__":
    unittest.main()
