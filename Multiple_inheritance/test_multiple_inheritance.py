import unittest
from io import StringIO
import sys
from multiple_inheritance import Bird, Fish

class TestMultipleInheritance(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_bird(self):
        bird = Bird()

        bird.speak()
        self.assertEqual(self.captured_output.getvalue().strip(), "Animal speaks")

        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        bird.chirp()
        self.assertEqual(self.captured_output.getvalue().strip(), "Chirping")

        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        bird.fly()
        self.assertEqual(self.captured_output.getvalue().strip(), "Flying")

    def test_fish(self):
        fish = Fish()

        fish.speak()
        self.assertEqual(self.captured_output.getvalue().strip(), "Animal speaks")

        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        fish.splash()
        self.assertEqual(self.captured_output.getvalue().strip(), "Splashing")


if __name__ == '__main__':
    unittest.main()