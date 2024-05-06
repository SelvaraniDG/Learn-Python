import unittest
from calculator import add, subtract, multiply, divide, exponentiate, modulus

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, -1), 2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 0), 0)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(-6, 3), -2)
        self.assertRaises(ZeroDivisionError, divide, 10, 0)  # Testing division by zero

    def test_exponentiate(self):
        self.assertEqual(exponentiate(2, 3), 8)
        self.assertEqual(exponentiate(4, 0), 1)
        self.assertEqual(exponentiate(0, 4), 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(5, 5), 0)
        self.assertRaises(ZeroDivisionError, modulus, 10, 0)  # Testing modulus by zero

if __name__ == '__main__':
    unittest.main()