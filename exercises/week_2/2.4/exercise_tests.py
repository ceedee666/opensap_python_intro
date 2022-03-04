from exercise import *
from unittest import mock
import unittest
import io

with mock.patch('builtins.input', side_effect=["This is how it should look like", "i"]):
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        exercise()

    assert fake_stdout.getvalue() == 'Ths s how t should look lke'