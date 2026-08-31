mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(type(mytuple))

'''
Same as list we can access tuple items by index and slicing and even methods 
and fuctions used in list can be used in tuple too but we cannot change the items in tuple as it is immutable.
'''

# Unpacking Tuples

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Tuple Methods

"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""

