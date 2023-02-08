class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"{self.name} makes a {sound} sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("The dog barks.")

dog = Dog("Max", "Labrador")
dog.make_sound("bark")


# Abstraction: 
# - Abstraction will be making `make_sound` method available to the user without displaying whats happening inside the method

# Encapsulation: 
# - It is about wrapping the data and methods within a class and protecting them from being changed by other classes.

# Inheritance: 
# - the Dog class is derived from the Animal class and inherits its properties and methods, such as make_sound.

# Polymorphism:
# - ability to override `make_sound` method after inheriting all the instance attributes and methods
