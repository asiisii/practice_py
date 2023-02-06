# Syntax
# create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Ordered, Unchangeable, allows duplicates

# Python - Access Tuple Items
# same as list

# access the first element
first_element = my_tuple[0]
print(first_element) # prints 1

# access the last element
last_element = my_tuple[-1]
print(last_element) # prints 5

# access a slice of elements
some_elements = my_tuple[1:3]
print(some_elements) # prints (2, 3)

# iterate over the elements
for element in my_tuple:
    print(element)


# Python - Update Tuples

# convert the tuple to a list, 
# modify the elements of the list, 
# and then convert the list back to a tuple

# create a tuple
my_tuple = (1, 2, 3, 4, 5)

# convert the tuple to a list
my_list = list(my_tuple)

# modify the elements of the list
my_list[0] = 10
my_list[-1] = 50

# convert the list back to a tuple
my_tuple = tuple(my_list)
print(my_tuple) # prints (10, 2, 3, 4, 50)


# Python - Unpack Tuples

# when you have a tuple with multiple values and you want to assign each value to a different variable

# create a tuple
my_tuple = (1, 2, 3, 4 , 5, 6)

# unpack the tuple into separate variables
a, b, *c = my_tuple

print(a) # prints 1
print(b) # prints 2
print(c) # prints [3, 4, 5, 6, 7]


# Discard unwanted elements: You can use an underscore (_) to discard the unwanted elements of the tuple when unpacking:

# unpack only the first two elements
a, b, *_ = my_tuple

print(a) # prints 1
print(b) # prints 2

# 
a, *b, c = my_tuple

print(a) # prints 1
print(b) # prints [2, 3, 4 ,5]
print(c) # prints 7


#  Python - Loop Tuples
for x in my_tuple:
  print(x)

for i in range(len(my_tuple)):
  print(my_tuple[i])

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
