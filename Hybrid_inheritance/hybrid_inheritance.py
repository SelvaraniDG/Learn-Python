class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

class Bird(Animal):
    def chirp(self):
        print("Bird chirps")

class Pet:
    def play(self):
        print("Pet is playing")


class PetDog(Dog, Pet):
    def fetch(self):
        print("Dog is fetching")

class PetCat(Cat, Pet):
    def scratch(self):
        print("Cat is scratching")

class PetBird(Bird, Pet):
    def sing(self):
        print("Bird is singing")


pet_dog = PetDog()
pet_cat = PetCat()
pet_bird = PetBird()

pet_dog.speak()  
pet_dog.bark()   
pet_dog.play() 
pet_dog.fetch()  

pet_cat.speak()   
pet_cat.meow()    
pet_cat.play()    
pet_cat.scratch() 

pet_bird.speak() 
pet_bird.chirp() 
pet_bird.play() 
pet_bird.sing() 