import unittest
import calculator


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 4), 5)
        self.assertEqual(calculator.add(3, -5), -2)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(2, 4), -2)
        self.assertEqual(calculator.subtract(4, 4), 0)
        self.assertEqual(calculator.subtract(14, 4), 10)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 5), 10)
        self.assertEqual(calculator.multiply(10, 0), 0)
        self.assertEqual(calculator.multiply(5, -4), -20)

    def test_division(self):
        self.assertEqual(calculator.division(10, 2), 5)
        self.assertEqual(calculator.division(2, 2), 1)
        self.assertRaises(ZeroDivisionError, calculator.division, 4, 0)


if __name__ == '__main__':
    unittest.main()
