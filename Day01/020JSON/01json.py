# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) # 30


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)



# ------------     Convert Python objects into JSON strings, and print the values:
print('------------ Python objects of the following types, into JSON strings')
print(json.dumps({"name": "John", "age": 30})) #{"name": "John", "age": 30}
print(json.dumps(["apple", "bananas"])) #["apple", "bananas"]
print(json.dumps(("apple", "bananas"))) #["apple", "bananas"]
print(json.dumps("hello")) #"hello"
print(json.dumps(42)) # 42
print(json.dumps(31.76)) # 31.76
print(json.dumps(True)) # true
print(json.dumps(False)) # false
print(json.dumps(None)) #null


print('------------Convert a Python object containing all the legal data types')

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

print(json.dumps(x, indent=4))
'''
{
    "name": "John",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}
'''
