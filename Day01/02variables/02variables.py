# Variables name are case - sensitive
a = 2
A = 3
# A doesn't overwrite the value for 'a'

x,y,z = 'orange', 'apple', 'cherry'
#  x = orange ~~~~ y = apple ~~~~~~ z = cherry

fruits = ['apple', 'banana', 'cherry']
x,y,z = fruits
# x = apple, y = banana, z = cherry


# Global variables

# there are two ways of creating a global variable
  # 1 x = "test"
  #2 using the keyword "global"

# we can also update the global variable from within the function
x = "hello"
def myFunc():
  global x
  x = "hello world"
myFunc()

#  when we print the x value it will return hello world
