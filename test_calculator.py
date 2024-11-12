# test_calculator.py

import unittest
from calculator import circle

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This method is run before each test, useful for setup code.
        self.calc = circle()

    def test_area(self):
        # Test addition functionality
        result = self.calc.area(3)
        self.assertEqual(result, 28.26)

    def test_perimeter(self):
        # Test subtraction functionality
        result = self.calc.parimeter(10)
        self.assertEqual(result, 62.800000000000004)


if __name__ == '__main__':
    unittest.main()
