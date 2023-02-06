# Syntax 
['one', 1, True, False, -1]

# can use the list() constructor to create list
mylist = list((1,2,True, False, "Hello"))
# [1, 2, True, False, 'Hello']


# Python - Access List Items
mylist[1]  # 2
mylist[-1] # 'Hello'
mylist[:3] # [1,2, True] 
mylist[1:] # [2, True, False, 'Hello']

# Python - Change List Items
mylist[0] = 10
mylist[0:1] = [10, 20] #[10, 20, True, False, 'Hello']
mylist.insert(0, -1)  # [-1, 1, 2, True, False, 'Hello']
mylist.append('World') # [1, 2, True, False, 'Hello', 'World']
mylist.extend(['apple', 'banana']) # [1, 2, True, False, 'Hello', 'apple', 'banana']
mylist.extend(('apple', 'banana')) # [1, 2, True, False, 'Hello', 'apple', 'banana']
mylist.remove(1) # [1, True, False, 'Hello']
mylist.pop(1) # 2 and will update the mylist to be [1, True, False, 'Hello']
mylist.pop() #removes the last item
del mylist[0] # will remove the first index
del mylist # will delete mylist
mylist.clear() # will empty the mylist

# Python - Loop Lists
for x in mylist:            #or  [print(x) for x in thislist]
  print(x)

for i in range(len(mylist)):
  print(mylist[i])


i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1

# Python - List Comprehension
mylist = list((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, True, False))
# [expression for item in iterable if condition]
[print(x) for x in mylist if x >= 0]

newlist = ['even' if x % 2 == 0 else 'odd' for x in mylist]

# Python - Sort Lists

thislist = [100, 50, 65, 82, 23]
thislist.sort() # [23, 50, 65, 82, 100]
thislist.sort(reverse=True) # [100, 82, 65, 50, 23]


def myfunc(n):
  return abs(n - 50)

thislist.sort(key = myfunc) # [50, 65, 23, 82, 100]


