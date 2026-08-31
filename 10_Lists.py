thisisalist = ["apple", "banana", "cherry"]               # Allow Duplicates, Can Be Any Data Type
print(thisisalist)                                       
print(len(thisisalist))
print(type(thisisalist))

print(list(("Saran","A2D","Rahul M")))

# Access List Items

print(thisisalist[1])                                     # Positive and Negative Indexing
print(thisisalist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change List Items

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist.insert(2, "watermelon")                         # We can Insert Items in list
print(thislist)


# Add list Items

thislist.append("orange")                                # we can just add items too then extend too
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove list Items

'''
thisisalist.remove("Cherry")
print(thisisalist)
'''

thisisalist.pop(1)
print(thisisalist)


thisisalist.clear()
print(thisisalist)

del thislist                                            # del keyword delete whole list by including memory


# Loop List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


for i in range(len(thislist)):
  print(thislist[i])


i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

[print(x) for x in thislist]

# List Comprehension

"""
Syntax
newlist = [expression for item in iterable if condition == True]
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
newlist1 = [x for x in range(10) if x < 5]
print(newlist1)
print(newlist)

# Sort List

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Copy List

thislist1 = ["apple", "banana", "cherry"]
mylist = thislist1.copy()
print(mylist)

# Join List

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

for x in list2:
  list1.append(x)

print(list1)

list1.extend(list2)
print(list1)

"""
append()	        Adds an element at the end of the list
clear()	            Removes all the elements from the list
copy()	            Returns a copy of the list
count()	            Returns the number of elements with the specified value
extend()	        Add the elements of a list (or any iterable), to the end of the current list
index()	            Returns the index of the first element with the specified value
insert()	        Adds an element at the specified position
pop()	            Removes the element at the specified position
remove()	        Removes the item with the specified value
reverse()	        Reverses the order of the list
sort()	            Sorts the list
"""
