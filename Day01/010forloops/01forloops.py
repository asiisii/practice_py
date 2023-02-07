# A for loop is used for iterating over a sequence \
# (that is either a list, a tuple, a dictionary, a set, or a string).

for x in range(6):
  print(x) # 0 1 2 3 4 5

for x in range(2, 6):
  print(x) # 2 3 4 5


for x in range(2, 30, 3):   #increment by 3
  print(x)   # 2 5 8 11 ...


# The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for x in range(6):
  print(x)
else:
  print("Finally finished!")



# nested 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
