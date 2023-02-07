# Python If ... Else
# syntax
'''
if condition1:
  execute this
elif condition2:
  execute this
else:
  execute this
'''
x = 10

if x > 20:
    print("x is greater than 20")
elif x > 15:
    print("x is greater than 15 but less than or equal to 20")
else:
    print("x is less than or equal to 15")



x = 10
#           value_if_true        if condition   else            value_if_false
result = "x is greater than 20"  if x > 20      else    "x is less than or equal to 20"


# if      condition    :              value_if_true
if         a > b       :        print("a is greater than b")



a = 330
b = 330
c = 500

if a > b:
    print("A")
elif a == b:
    print("=")
else:
    print("B")

#      is same as 

print("A") if a > b else print("=") if a == b else print("B")


if a > b and c > a:
  print("Both conditions are True")

if a > b or a > c:
  print("At least one of the conditions is True")

if not a > b:
  print("a is NOT greater than b")


if b > a:
  pass
# The pass statement in the if block serves as a placeholder, indicating that there is supposed to be some code here, but for now we don't want it to do anything
