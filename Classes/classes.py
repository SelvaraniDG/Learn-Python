class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating objects of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing object attributes and calling method
person1.introduce() 
person2.introduce()