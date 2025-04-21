import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        # Arrange
        a = 2
        b = 3
        expected = 5
        # Act
        result = self.calc.add(a, b)
        # Assert
        self.assertEqual(result, expected)

    def test_add_negative_and_positive(self):
        a = -5
        b = 10
        expected = 5
        result = self.calc.add(a, b)
        self.assertEqual(result, expected)

    def test_subtract_smaller_from_bigger(self):
        a = 10
        b = 3
        expected = 7
        result = self.calc.subtract(a, b)
        self.assertEqual(result, expected)

    def test_subtract_bigger_from_smaller(self):
        a = 3
        b = 10
        expected = -7
        result = self.calc.subtract(a, b)
        self.assertEqual(result, expected)

    def test_multiply_with_positive(self):
        a = 4
        b = 5
        expected = 20
        result = self.calc.multiply(a, b)
        self.assertEqual(result, expected)

    def test_multiply_with_zero(self):
        a = 0
        b = 100
        expected = 0
        result = self.calc.multiply(a, b)
        self.assertEqual(result, expected)

    def test_divide_normal(self):
        a = 10
        b = 2
        expected = 5
        result = self.calc.divide(a, b)
        self.assertEqual(result, expected)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
