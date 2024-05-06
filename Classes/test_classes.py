import unittest
from classes import Person

class TestPerson(unittest.TestCase):
    def test_introduce(self):
        # Create instances of the Person class
        person1 = Person("Alice", 30)
        person2 = Person("Bob", 25)

        # Redirect stdout to capture print output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the introduce method
        person1.introduce()
        person2.introduce()

        # Get the printed output
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()

        # Check if the output matches the expected format
        expected_output = "My name is Alice and I am 30 years old.\nMy name is Bob and I am 25 years old."
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()