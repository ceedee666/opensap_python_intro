from exercise import *
from unittest import mock
import unittest
import io

with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
    palindrome()

assert palindrome("89kjhg \\~~\\ ghjk98") == True, "Die Funktion funktioniert nicht korrekt. Das Pallindrom 89kjhg \\~~\\ ghjk98 wurde nicht erkannt.\"\n"
assert palindrome("89kjhghjk98") == True, "Die Funktion sollte auch bei Zeichenketten ungerader Länge funktionieren\"\n"
assert palindrome("Lagerregal") == True, "Die Funktion sollte Groß-/Kleinschreibung ignorieren.\"\n"