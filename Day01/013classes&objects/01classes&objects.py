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

    def __str__(self):
      return f"{self.name} is a {self.age} year old {self.breed}"

dog = Dog("Fido", "Labrador", 3)

print(dog.name)  # Output: Fido
dog.bark()  # Output: Fido barks!


# self is a reference to the instance of the class and is used to access its attributes and methods.

#  __init__
# The __init__ method is called a constructor and is automatically called when an object of the class is created. 

#  __str__
# The __str__ method is used to provide a human-readable representation of an object. 
# It is called when you use the built-in str() function or the print function on an object, 
# and it should return a string that represents the object



# class definitions cannot be empty, but if you for some reason have a class definition with no content, 
# put in the pass statement to avoid getting an error.
class Person:
  pass
