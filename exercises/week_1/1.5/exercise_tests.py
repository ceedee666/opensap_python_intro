from exercise import *
import unittest

class ExerciseTests(unittest.TestCase):
    def test_input_digit(self):
        result = name.isdigit()
        if result == True:   
            raise ValueError('Please enter a name!')

if __name__ == '__main__':
    unittest.main()



    