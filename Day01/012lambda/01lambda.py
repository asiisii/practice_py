# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.


# Syntax
# lambda arguments : expression


add = lambda x, y: x + y
result = add(3, 4)
print(result) # Output: 7


# They are commonly used as arguments to higher-order functions (functions that take other functions as arguments). 

numbers = [1, 3, 5, 2, 4]
sorted_numbers = sorted(numbers, key=lambda x: -x)
print(sorted_numbers) # Output: [5, 4, 3, 2, 1]

