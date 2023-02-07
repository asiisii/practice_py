# Syntax
myset = { 1, 2, 3, 4 }

# unordered 
# unchangeable - but can remove and add items
# unindexed 
# duplicates NOT allowed


# Sets are unchangeable because they are unindexed, meaning that they don't have any order or positional relationship between their elements. Therefore, you can't access or update individual elements of a set by their index. Instead, you can add or remove elements to or from a set as a whole, but you can't modify individual elements within the set.

myset.remove(4)
myset.add(5)

# if you try to remove elements that doesn't exist in the set it will give an error
# if you add existing element then it won't get added


# Python - access set

if 3 in myset:
    print("3 exists in the set")


#  Python - Add Set Items 

myset.add(5)

#  if we have another set or any other iteratable data then we can use update

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

fruits.update(more_fruits)


# Python - Remove Set Items

myset.remove(4) # it will throw an error if we try to remove nonexisting item
myset.discard(4) # doesn't throw error if we try to nonexisting item
myset.pop() #removes random item
myset.clear() # myset will equal set()
del myset # will delete everything including the variable


# Python - Join Sets
myset1 = { 1, 2, 3 , 4 }
myset2 = { 1, 5, 6 }
myset3 = myset1.union(myset2)
# or 
myset3 = myset1 | myset2
# both will return myset3 = { 1, 2, 3, 4, 5, 6}

myset1.update(myset2) #will update the variable myset1

myset1.intersection_update(myset2) # myset1 will be {1} it will only keep the common item from both set
myset1.intersection(myset2) # it will return new set, that contains items that are common in both set

myset1.symmetric_difference_update(myset2) # myset1 will have items that are not present on both set
myset1.symmetric_difference(myset2) # will reutrn new set, of items that are not present on both set
