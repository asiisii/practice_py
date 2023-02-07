i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


i = 1
while i <= 5:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

# Output: 1
#         3
#         5


# In this example, the while loop iterates as long as i is less than or equal to 5.
# The if statement checks if i is even. If i is even, the continue statement is executed
# and the rest of the code in the current iteration is skipped. The loop then continues
# with the next iteration, and the value of i is incremented by 1. If i is not even,
# the print statement is executed and the value of i is printed, followed by incrementing i by 1.

