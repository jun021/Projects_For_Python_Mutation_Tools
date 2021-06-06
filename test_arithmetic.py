import unittest
import arithmetic

class TestArithmetic (unittest.TestCase):

    def test_square(self):
        num = 5
        result = arithmetic.take_square(num)
        self.assertEqual(result, 25)

    def test_cube(self):
        num = 3
        result = arithmetic.take_cube(num)
        self.assertEqual(result, 81)

    def test_power(self):
        num1 = 2
        num2 = 6

        result = arithmetic.take_power(num1, num2)
        self.assertEqual(result, 64)   