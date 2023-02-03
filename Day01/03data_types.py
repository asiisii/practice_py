#  str
x = "Hello World"		
# int
x = 20
# float 
x = 20.5
x = 35e3
y = 12E4
z = -87.7e100
# complex	= are written with a "j" as the imaginary part
x = 1j
# list	
x = ["apple", "banana", "cherry"]
# tuple	
x = ("apple", "banana", "cherry")
# range	
x = range(6)
# dict	
x = {"name" : "John", "age" : 36}	
# set
x = {"apple", "banana", "cherry"}	
# frozenset
x = frozenset({"apple", "banana", "cherry"})
# bool	
x = True
# bytes	
x = b"Hello"
# bytearray	
x = bytearray(5)
# memoryview	
x = memoryview(bytes(5))
# NoneType	
x = None	


# data conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)



#  to generate random number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers
import random

print(random.randrange(1, 10))


