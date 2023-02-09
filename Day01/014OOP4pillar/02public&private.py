'''
in python theres no public or private keyword we can use like in Java to make variable and method privates
adding underscore infront of variable or method is a convention of saying this is private but doesn't stop
us from updating it
'''
class MyClass:
    def __init__(self):
        self._private_attribute = 42

    def _private_method(self):
        print("This is a private method.")
