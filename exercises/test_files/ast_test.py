import ast
from pprint import pprint


def main():
    with open("test_exercise.py", "r") as source:
        tree = ast.parse(source.read())

    analyzer = Analyzer()
    analyzer.visit(tree)
    analyzer.report()


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"ifs": []}

    def visit_If(self, node):
        self.stats["ifs"].append(node.lineno)
        self.generic_visit(node)

    def report(self):
        pprint(self.stats)


if __name__ == "__main__":
    main()
