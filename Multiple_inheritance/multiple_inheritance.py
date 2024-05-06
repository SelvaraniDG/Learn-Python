class Animal:
    def speak(self):
        print("Animal speaks")

class Flyable:
    def fly(self):
        print("Flying")

class Swimmable:
    def swim(self):
        print("Swimming")

class Bird(Animal, Flyable):  
    def chirp(self):
        print("Chirping")

class Fish(Animal, Swimmable):
    def splash(self):
        print("Splashing")


bird = Bird()
fish = Fish()
bird.speak() 
bird.chirp() 
bird.fly()
fish.speak()  
fish.splash() 
