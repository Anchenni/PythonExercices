# Python3 program for explaining
# use of list, tuple, set and 
# dictonary
  
# Lists
l = []
  
# Adding Element into list
l.append(5)
l.append(10)
print("Adding 5 and 10 in list", l)
  
# Popping Elements from list
l.pop()
print("Popped one element from list", l)
print()
  
# Set
s = set()
  
# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)
  
# Removing element from set
s.remove(5)
print("Removing 5 from set", s)
print()
  
# Tuple
t = tuple(l)
  
# Tuples are immutable
print("Tuple", t)
print()
  
# Dictonary
d = {}
  
# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictonary", d)
  
# Removing key-value pair
del d[10]
print("Dictonary", d)
"""
List:

Used in JSON format
Useful for Array operations
Used in Databases
Tuple:

Used to insert records in the database through SQL query at a time
Ex: (1.’sravan’, 34).(2.’geek’, 35)
Used in parentheses checker
Set

Finding unique elements
Join operations
Dictionary

Used to create a data frame with lists
Used in JSON
"""