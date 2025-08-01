#https://github.com/theg2000/lab10-TH
#Partner 1: Trevor Hegarty

import unittest
import math
import calculator  

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(calculator.div(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5, 0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -8)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
