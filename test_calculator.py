import unittest
import math
import calculator  

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.log(-2, 8)
        with self.assertRaises(ValueError):
            calculator.log(2, -8)
        with self.assertRaises(ValueError):
            calculator.log(0, 10)

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
