# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# convert decimal to binary

# eg: 10

10/2 = 5      remainder 0
5/2 = 2       remainder 1
2/2 = 1       remainder 0
1/2 = 0       remainder 1

binary = 1010

convert 1010 to decimal

1          0            1             0
2^3=8     2^2=4         2^1=2         2^0 = 1
8 + 0 + 2 = 10    <- we dont add the number of 0 placeholder


x = 5    #0101
# 0011 = 3
x &= 3    (x = x & 3)

  0101
+ 0011
-------
  0001 = 1 decimal


x |= 3    (x = x | 3)

  0101
+ 0011
-------
  0111 = 7 decimal      #if theres at least one 1 then the sum will be 1


x ^= 3    (x = x ^ 3)
  0101
+ 0011
-------
  0110 = 6 decimal     #opposite of &=


x >>= 3
0101 will be 0001 = 1 decimal

x <<= 3
0101 will be 0101000 = 40 decimal


#````````````logical `
and 	#Returns True if both statements are true	x < 5 and  x < 10	
or	  #Returns True if one of the statements is true	x < 5 or x < 4	
not	  #Reverse the result, returns False if the result is true	not(x < 5 and x < 10)


#```````````````Python Membership Operators`````````````````
x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list



x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list
