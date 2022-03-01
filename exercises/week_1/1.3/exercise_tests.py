from exercise import *
import unittest

class ExerciseTests(unittest.TestCase):
    def test_input(self):
        try:
            val = int(str(i)) or int(str(j))
        except ValueError:
            print("That's not a number!")
    
    def test_sum_or_mult(self):
        try:
            i - j or i / j or j - i or j / i
        except:
            self.assertFalse(i)


    