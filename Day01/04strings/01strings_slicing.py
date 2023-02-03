# can assign a multiline string to a variable by using three quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''


# string are arrays
x = 'hello'
x[0] #this will return 'h'

#  looping through string 

for x in "banana":
  print(x)

#  use len() method to get length of the string


# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)


# Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


# Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)


# Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5]) #ello


# Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

# Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

'''
Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
'''
b = "Hello, World!"
print(b[-5:-2])
