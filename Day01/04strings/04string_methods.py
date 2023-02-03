#  capitalize()	#Converts the first character to upper case
text = "this is a string"
print(text.capitalize()) #Output: "This is a string"

# casefold()	#Converts string into lower case
text = "HELLO, World!"
print(text.casefold()) #Output: "hello, world!"

# center()	#Returns a centered string
text = "python"
print(text.center(10, "*")) #Output: "***python***"

# count()	#Returns the number of times a specified value occurs in a string
text = "Hello, World!"
substring = "l"
print(text.count(substring)) #Output: 3

# encode()	#Returns an encoded version of the string
text = "Hello, World!"
print(text.encode()) #Output: b'Hello, World!'

# endswith()	#Returns true if the string ends with the specified value
text = "Hello, World!"
suffix = "World!"
print(text.endswith(suffix)) #Output: True

# expandtabs()	#Sets the tab size of the string
text = "Hello\tWorld!"
print(text.expandtabs(10)) #Output: "Hello     World!"

# find()	#Searches the string for a specified value and returns the position of where it was found
text = "Hello, World!"
substring = "l"
print(text.find(substring)) #Output: 2

# format()	#Formats specified values in a string
text = "Hello, {}!"
name = "World"
print(text.format(name)) #Output: "Hello, World!"

# format_map()	#Formats specified values in a string
text = "Hello, {name}!"
data = {"name": "World"}
print(text.format_map(data)) #Output: "Hello, World!"

# index()	#Searches the string for a specified value and returns the position of where it was found
text = "Hello, World!"
substring = "l"
print(text.index(substring)) #Output: 2

# isalnum()	#Returns True if all characters in the string are alphanumeric
text = "Hello123"
print(text.isalnum()) #Output: True

# isalpha()	#Returns True if all characters in the string are in the alphabet
text = "Hello"
print(text.isalpha()) #Output: True

# isdecimal()	#Returns True if all characters in the string are decimals
text = "123"
print(text.isdecimal()) #Output: True

# isdigit()	#Returns True if all characters in the string are digits
text = "123"
print(text.isdigit()) #Output: True

# isidentifier()	#Returns True if the string is an identifier
text = "hello"
print(text.isidentifier()) #Output: True

# islower()	#Returns True if all characters in the string are lower case
text = "hello"
print(text.islower()) #Output: True

# isnumeric()	#Returns True if all characters in the string are numeric
text = "123"
print(text.isnumeric()) #Output: True

# isprintable()	#Returns True if all characters in the string are printable
text = "Hello\nWorld!"
print(text.isprintable()) #Output: False

# isspace()	#Returns True if all characters in the string are whitespaces
text = " "
print(text.isspace()) #Output: True

# istitle()	#Returns True if the string follows the rules of a title
text = "Hello, World!"
print(text.istitle()) #Output: False

# isupper()	#Returns True if all characters in the string are upper case
text = "HELLO"
print(text.isupper()) #Output: True

# join()	#Joins the elements of an iterable to the end of the string
text = ","
words = ["Hello", "World"]
print(text.join(words)) #Output: "Hello,World"

# ljust()	#Returns a left justified version of the string
text = "Hello"
print(text.ljust(10, "*")) #Output: "Hello*****"

# lower()	#Converts a string into lower case
text = "HELLO, WORLD!"
print(text.lower()) #Output: "hello, world!"

# lstrip()	#Returns a left trim version of the string
text = " Hello, World!"
print(text.lstrip()) #Output: "Hello, World!"

# maketrans()	#Returns a translation table to be used in translations
text1 = "abc"
text2 = "def"
translation_table = text1.maketrans(text1, text2)
print(translation_table) #Output: {97: 100, 98: 101, 99: 102}

# partition()	#Returns a tuple where the string is parted into three parts
text = "Hello, World!"
substring = ","
print(text.partition(substring)) #Output: ('Hello', ',', ' World!')

# replace()	#Returns a string where a specified value is replaced with a specified value
text = "Hello, World!"
old = "World"
new = "Universe"
print(text.replace(old, new)) #Output: "Hello, Universe!"

# rfind()	#Searches the string for a specified value and returns the last position of where it was found
text = "Hello, World!"
substring = "l"
print(text.rfind(substring)) #Output: 9

# rindex()	#Searches the string for a specified value and returns the last position of where it was found
text = "Hello, World!"
substring = "l"
print(text.rindex(substring)) #Output: 9

# rjust()	#Returns a right justified version of the string
text = "Hello"
print(text.rjust(10, "*")) #Output: "*****Hello"

# rpartition()	#Returns a tuple where the string is parted into three parts
text = "Hello, World!"
substring = ","
print(text.rpartition(substring)) #Output: ('Hello', ',', ' World!')

# rsplit()	#Splits the string at the specified separator, and returns a list
text = "Hello, World!"
print(text.rsplit(", ")) #Output: ['Hello', 'World!']

# rstrip()	#Returns a right trim version of the string
text = "Hello, World! "
print(text.rstrip()) #Output: "Hello, World!"

# split()	#Splits the string at the specified separator, and returns a list
text = "Hello, World!"
print(text.split(", ")) #Output: ['Hello', 'World!']

# splitlines()	#Splits the string at line breaks and returns a list
text = "Hello\nWorld!"
print(text.splitlines()) #Output: ['Hello', 'World!']

# startswith()	#Returns true if the string starts with the specified value
text = "Hello, World!"
prefix = "Hello"
print(text.startswith(prefix)) #Output: True

# strip()	#Returns a trimmed version of the string
text = " Hello, World! "
print(text.strip()) #Output: "Hello, World!"

# swapcase()	#Swaps cases, lower case becomes upper case and vice versa
text = "Hello, World!"
print(text.swapcase()) #Output: "hELLO, wORLD!"

# title()	#Converts the first character of each word to upper case
text = "hello, world!"
print(text.title()) #Output: "Hello, World!"

# translate()	#Returns a translated string
text = "abc"
translation_table = text.maketrans("ab", "cd")
print(text.translate(translation_table)) #Output: "cdc"

# upper()	#Converts a string into upper case
text = "hello, world!"
print(text.upper()) #Output: "HELLO, WORLD!"

# zfill()	#Fills the string with a specified number of 0 values at the beginning
text = "Hello"
print(text.zfill(10)) #Output: "00000Hello"


