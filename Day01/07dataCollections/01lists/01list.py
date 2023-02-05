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
