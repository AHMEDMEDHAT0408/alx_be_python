import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Add more assertions to thoroughly test the subtract method.

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        # Add more assertions to thoroughly test the multiply method.

    def test_division(self):
        """Test the divide method."""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        # Add more assertions to thoroughly test the divide method.

if __name__ == "__main__":
    unittest.main()
