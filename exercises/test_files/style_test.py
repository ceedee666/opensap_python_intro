import unittest

from pylint import epylint as lint

class Assess(unittest.TestCase):
    def test_style(self):
        pylint_opts = ['--rcfile=default.pylintrc']
        self.assertEqual(0, lint.lint('exercise.py', options=pylint_opts), "PyLint did not exit successfully")
