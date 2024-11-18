import unittest
from src.calculator import Calculator  # Assuming the Calculator class is saved in calculator.py

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up a Calculator instance for each test."""
        self.calc = Calculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_sub(self):
        """Test the static sub method."""
        self.assertEqual(Calculator.sub(5, 3), 2)
        self.assertEqual(Calculator.sub(0, 0), 0)
        self.assertEqual(Calculator.sub(7, -2), 9)
        self.assertEqual(Calculator.sub(-5, -5), 0)

    def test_mul(self):
        """Test the mul method."""
        self.assertEqual(self.calc.mul(2, 3), 6)
        self.assertEqual(self.calc.mul(-1, 5), -5)
        self.assertEqual(self.calc.mul(0, 10), 0)
        self.assertEqual(self.calc.mul(-4, -3), 12)

if __name__ == "__main__":
    unittest.main()
