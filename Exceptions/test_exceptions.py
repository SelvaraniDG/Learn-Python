import unittest
from io import StringIO
import sys
from exceptions import divide

class TestDivideFunction(unittest.TestCase):
    def test_divide_by_zero(self):
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the divide function with division by zero
        divide(10, 0)

        # Get the printed output
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()

        # Check if the error message is printed
        self.assertIn("Error: Division by zero!", output)
        self.assertIn("Division operation completed.", output)

    def test_divide_normal_case(self):
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the divide function with a normal case
        divide(10, 2)

        # Get the printed output
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()

        # Check if the result message is printed
        self.assertIn("Result of division: 5.0", output)
        self.assertIn("Division operation completed.", output)

if __name__ == '__main__':
    unittest.main()