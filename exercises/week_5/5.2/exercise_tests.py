from exercise import *
from unittest import mock
import unittest
import io

with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
    rect_area()

assert rect_area(5, 7) == 35, "Die Funktion funktioniert nicht korrekt. Die Fläche eines Rechecks mit den Seiten 5 und 7 sollte 35 sein."
assert rect_area(length = 5, width = 7) == 35, "Die Parameter haben nicht die vorgegebenen Namen"
assert rect_area(length = 7) == 49, "Die Funktion sollte auch funktionieren wenn nur die Länge übergeben wird."