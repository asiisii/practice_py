#  Python - DocStrings

# helps to document the program better

def test(num):
    '''This is the syntax for docString and where we describe our program
  
    leave the second line empty and end the sentence with a period.'''
    if num % 2 == 0:
        print('even number')
    else:
        print('odd number')


print(test(10))
print(test.__doc__)

# even number
# This is the syntax for docString and where we describe our program

    # leave the second line empty and end the sentence with a period.'




# using __doc__ method we can get the docStrings value
#  will be helpful for other programmer before using the module
