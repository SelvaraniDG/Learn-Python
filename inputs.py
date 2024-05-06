import unittest
from io import StringIO
import sys
from mock import patch  # Import patch from mock module

def get_user_input():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    phone_number = input("Enter your phone number: ")
    return name, age, phone_number

def display_details(name, age, phone_number):
    print("-------------------------------")
    print("Your details")
    print("-------------------------------")
    print("Name:", name)
    print("Age:", age)
    print("Phone Number:", phone_number)

class TestUserDetails(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_display_details(self):
        # Simulate user input
        with patch('builtins.input', side_effect=['Alice', '30', '1234567890']):  # Use patch directly
            # Call the function under test
            name, age, phone_number = get_user_input()

        # Redirect stdout to capture print output
        with self.captured_output as output:
            # Call the function under test
            display_details(name, age, phone_number)

            # Get the printed output
            output_str = output.getvalue().strip()

        # Check if the output matches the expected format
        expected_output = (
            "-------------------------------\n"
            "Your details\n"
            "-------------------------------\n"
            "Name: Alice\n"
            "Age: 30\n"
            "Phone Number: 1234567890"
        )
        self.assertEqual(output_str, expected_output)

if __name__ == '__main__':
    unittest.main()