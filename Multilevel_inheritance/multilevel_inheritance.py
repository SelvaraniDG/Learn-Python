class Animal:
    def speak(self):
        print("Animal speaks")

class Pet(Animal):
    def play(self):
        print("Pet is Playing")

class Dog(Pet):
    def bark(self):
        print("Dog barks")

class Poodle(Dog):
    def groom(self):
        print("Poodle is groomed")

poodle = Poodle()
poodle.speak() 
poodle.play()
poodle.bark() 
poodle.groom() 
