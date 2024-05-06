import unittest
from io import StringIO
import sys

from hybrid_inheritance import Animal, Dog, Cat, Bird, Pet, PetDog, PetCat, PetBird

class TestAnimalClasses(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_pet_dog(self):
        pet_dog = PetDog()
        pet_dog.speak()
        self.assertEqual(self.captured_output.getvalue().strip(), "Animal speaks")

        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        pet_dog.bark()
        self.assertEqual(self.captured_output.getvalue().strip(), "Dog barks")

        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        pet_dog.play()
        self.assertEqual(self.captured_output.getvalue().strip(), "Pet is playing")

        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        pet_dog.fetch()
        self.assertEqual(self.captured_output.getvalue().strip(), "Dog is fetching")

    def test_pet_cat(self):
        pet_cat = PetCat()
        pet_cat.speak()
        self.assertEqual(self.captured_output.getvalue().strip(), "Animal speaks")

        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        pet_cat.meow()
        self.assertEqual(self.captured_output.getvalue().strip(), "Cat meows")

        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        pet_cat.play()
        self.assertEqual(self.captured_output.getvalue().strip(), "Pet is playing")

        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        pet_cat.scratch()
        self.assertEqual(self.captured_output.getvalue().strip(), "Cat is scratching")

    def test_pet_bird(self):
        pet_bird = PetBird()
        pet_bird.speak()
        self.assertEqual(self.captured_output.getvalue().strip(), "Animal speaks")

        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        pet_bird.chirp()
        self.assertEqual(self.captured_output.getvalue().strip(), "Bird chirps")

        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        pet_bird.play()
        self.assertEqual(self.captured_output.getvalue().strip(), "Pet is playing")

        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        pet_bird.sing()
        self.assertEqual(self.captured_output.getvalue().strip(), "Bird is singing")


if __name__ == '__main__':
    unittest.main()