import unittest
from io import StringIO
import sys
from multilevel_inheritance import Poodle

class TestAnimalClasses(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_poodle(self):
        poodle = Poodle()

        poodle.speak()
        sys.stdout.seek(0)
        output = sys.stdout.read().strip()

        self.assertEqual(output, "Animal speaks")

        # Reset the StringIO object
        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        poodle.bark()
        sys.stdout.seek(0)
        output = sys.stdout.read().strip()
        self.assertEqual(output, "Dog barks")

        #Reset the StringIO object
        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        poodle.play()
        sys.stdout.seek(0)
        output = sys.stdout.read().strip()
        self.assertEqual(output, "Pet is Playing")

        # Reset the StringIO object
        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        poodle.groom()
        sys.stdout.seek(0)
        output = sys.stdout.read().strip()
        self.assertEqual(output, "Poodle is groomed")

if __name__ == '__main__':
    unittest.main()