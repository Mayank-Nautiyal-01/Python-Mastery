
#* Data type = classification of data
# ? It tells :
# What kind of value it is
# What operations are allowed
# How it is stored in memory

#? Primitive data types → Simple values (int, float, bool)
#? Non-primitive data types → Collections (list, tuple, dict, set)

#! Numeric Types
#? int (Integer): Whole numbers. ex: x=-9

#? float :Decimal numbers. ex:pi = 3.14

#! Boolean Type
# Only two values:
# True
# False

# !Sequence Types: These store multiple values in order.

#? str (String) ex: name="mayank"
# Strings are immutable.
# lets see how:
# * 1: Try Modifying a Character
# name = "mayank"
# name[0] = "M"
# print(name): thow an error : name[0] = "M" TypeError: 'str' object does not support item assignment
#* That is immutability, Because the string object cannot be changed after creation.

#* 2: Memory Address Changes
name = "mayank"
# print(id(name)) 
# output :2394395693472
# id() returns the memory address of the object.
name = name + " nautiyal"
print(id(name))
# output:1846586293808

#*  now what did u see in both output :
# Two different memory addresses.
# Why?
# Because:
# Python did NOT modify the original string.
# It created a NEW string object.
# Then reassigned name to the new object.
# If strings were mutable:
# The memory address would remain the same.
# But it changes.

# ?list:Ordered, mutable collection.
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
# [1, 2, 3, 4]

#* as u see its mutable-lets see with an ex:
lst = [1, 2, 3]
print(id(lst))
# 1529450707392
lst.append(4)
print(id(lst))
# 1529450707392
# Same memory address.
# Because list is modified in-place.

#? tuple:Ordered, immutable collection.
point = (10, 20)
point[0]=12;
print(point)
# TypeError: 'tuple' object does not support item assignment
# note:Tuples don’t have append, remove, pop, etc.Because they cannot be changed,but list have these method coz it is mutable.

# !Set :Unordered collection of unique elements.
s = {1, 2, 3}
print(s)
# No duplicates allowed.
# if we use duplicates:
n={1,2,2,3,4}
print(n)
# output:{1, 2, 3, 4} it will provide it by removing that duplicate value
# *also:
# A set is:Unordered,Unique elements only,Mutable

# Ex:
s = {1, 2, 3}
s.add(4)
print(s)
# {1, 2, 3, 4}
# *but This Will Fail
s = {1, 2, 3}
s[0] = 10

# Error
# Why?
# Because sets are unordered.
# No indexing allowed.

# !Mapping Type: dict (Dictionary):Key-value pairs,Mutable,Ordered (Python 3.7+ maintains insertion order)
student = {
    "name": "mayank",
    "age": 21
}
print(student)
# {'name': 'mayank', 'age': 21}

student["age"] = 22
print(student)
# {'name': 'mayank', 'age': 22}
#* proof
d = {"a": 1}
print(id(d))
# 1113079670592
d["a"] = 2
print(id(d))
# 1113079670592

# Same memory address.
# Modified in place.


# -----------------------
# difference:
#* Immutable:
# Cannot change internal state
# Any "change" creates new object

#* Mutable:
# Can change internal state
# Same object modified