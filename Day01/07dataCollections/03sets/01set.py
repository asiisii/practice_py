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
