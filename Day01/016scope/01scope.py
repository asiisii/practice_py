#  Function inside a function

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc() # 300


# Global scope

x = 300

def myfunc():
  x = 200
  print(x) # 200

myfunc()

print(x) # 300

# -----------------------------------

x = 300

def myfunc():
  global x
  x = 200 # this will update the x value 

myfunc()

print(x) # 200
