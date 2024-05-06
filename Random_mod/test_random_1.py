import unittest
from io import StringIO
import sys
from random_1 import generate_random_numbers

class TestRandomNumberGenerator(unittest.TestCase):

    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_generate_random_numbers(self):
        num_times = 5
        generate_random_numbers(num_times)

if __name__ == '__main__':
    unittest.main()