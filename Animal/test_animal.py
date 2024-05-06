import unittest
from animal import Animal, Dog, Cat

class TestAnimal(unittest.TestCase):
    def test_dog_speak(self):
        dog = Dog("Doggy")
        self.assertEqual(dog.speak(), "Doggy says Woof!")

    def test_cat_speak(self):
        cat = Cat("Kitty")
        self.assertEqual(cat.speak(), "Kitty says Meow!")

if __name__ == '__main__':
    unittest.main()