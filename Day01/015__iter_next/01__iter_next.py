class MyRange:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        else:
            result = self.current
            self.current += 1
            return result


my_range = MyRange(5)
for i in my_range:
    print(i)

'''
first thing we need to do is make our instance `my_range` an iterator 
and for that we need def `__iter__` method returning self. 
And the method `__next__` is where we actually do the iteration 
and it will stop after there are no more items to be returned
'''

'''
The iterator protocol requires that an object implement the __iter__ method, which should return the object itself or an iterator object that can be used to iterate over the object's items. The __next__ method is then used to return the next item in the sequence, until there are no more items to be returned.

In the example of the MyRange class, the __iter__ method returns self, which is the my_range object itself, so the my_range object is an iterator. The __next__ method increments the current attribute and returns its value, until the current value is equal to or greater than the limit, at which point a StopIteration exception is raised to signal that there are no more items to be returned.
'''
