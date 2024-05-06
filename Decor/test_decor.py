import unittest
from decor import add_prefix, greet

class TestAddPrefixDecorator(unittest.TestCase):
    def test_add_prefix_decorator(self):
        result = greet("Alice")
        
        # Check if the prefix is added correctly
        self.assertEqual(result, "Prefix: Hello, Alice!")

if __name__ == '__main__':
    unittest.main()