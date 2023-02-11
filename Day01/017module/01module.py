# Module: 

#  same as code library
# A file containing a set of functions you want to include in your application


#  in file mymodule.py
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#  ------ now in different file -----
import mymodule

mymodule.greeting("Habibi")  #Hello, Habibi


a = mymodule.person1["age"]
print(a) # 36

#  if we want to import  only person1 we can
from mymodule import person1

print (person1["age"])



# can give alias to module 
import mymodule as greetingModule


#  there are alot of built-in methods
Import and use the platform module:

import platform

x = platform.system()
print(x)


x = dir(platform)
print(x)
