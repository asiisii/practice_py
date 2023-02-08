# Python Classes and Objects

#  class is like "blueprint" for creating objects


# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name) # John
print(p1.age) # 36


# another example

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} barks!")

dog = Dog("Fido", "Labrador", 3)

print(dog.name)  # Output: Fido
dog.bark()  # Output: Fido barks!


# The __init__ method is called a constructor and is automatically called 
# when an object of the class is created. 
# self is a reference to the instance of the class and is used to access its attributes and methods.
