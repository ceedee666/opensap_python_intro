from exercise import *
from unittest import mock
import unittest
import io

with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
    filesummer()

assert filesummer() != 5050, "Please redo the task, your output is wrong!"