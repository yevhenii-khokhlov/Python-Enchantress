import unittest

import homework.test_simple_calc as calc


class SimpleCalcTest(unittest.TestCase):
    """
    Class for making unittests of 'test_simple_calc.py'
    """

    def test_add(self):
        self.assertEqual(calc.add(1, 3), 4)
        self.assertEqual(calc.add(-2, 2), 0)

    def test_subtract(self):
        self.assertEqual(calc.subtract(1, 3), -2)
        self.assertEqual(calc.subtract(0, 0), 0)
        self.assertEqual(calc.subtract(3, 1), 2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(0, 0), 0)
        self.assertEqual(calc.multiply(1, 0), 0)
        self.assertEqual(calc.multiply(1, 3), 3)

    def test_divide(self):
        self.assertEqual(calc.divide(4, 2), 2.0)
        self.assertEqual(calc.divide(4, 1), 4.0)
        self.assertEqual(calc.divide(0, 4), 0.0)
        self.assertEqual(calc.divide(4, 4), 1.0)
        self.assertRaises(ValueError, lambda: calc.divide(5, 0))
        self.assertRaises(TypeError, lambda: calc.divide('one', 'two'))


if __name__ == "__main__":
    unittest.main()
