
#* What is a Variable?
#? => A variable is a name that refers to an object in memory.
# note:
# Variables do NOT store values directly.
# They store references to objects.

# let see with an ex:
#  x=10
#! before this ex i see a error which is IndentationError: unexpected indent 
#? This means:

# !👉 You added spaces (or a tab) at the beginning of a line where Python was not expecting indentation.so Indentation is only allowed:Inside functions,Inside loops,Inside if statements,Inside classes

# now move further to ex:
#? x = 10
#? What happens internally:
# ?An integer object 10 is created in memory.
# ?x points to that object.

#* Creating Variables:
name = "mayank"
age = 21
height = 5.8
is_student = True

# ?Python automatically decides the type.
# ?lets see their types which python decides:
print(type(name))
# output: <class 'str'>
print(type(age))
#output:<class 'int'>
print(type(height))
#output:<class 'float'>
print(type(is_student))
#output:<class 'bool'>

#!note:now u r thinking what is this class coming in every output,so :
# In Python everything is an object.Every object is created from a class
#     Even basic data types like:int,float,str,bool are actually classes
#? so int is a class
#? 10 is an object(instance of int) created from the int class
#? x is a reference pointing to that object

# *Naming Rules:
# ?Valid: 
# my_name = "A"
# _age = 20
# num1 = 100
# ?Invalid:
# 1name = "A"   # Cannot start with number
# my-name = 10  # Hyphen not allowed
#? Rules: same as other language,nothing new (so u can skip):
# Must start with letter or underscore
# No spaces
# Case-sensitive (age ≠ Age)
# Cannot use reserved keywords (if, for, class, etc.)

# *Multiple Assignment:
a, b, c = 1, 2, 3
#  Swap variables:
x = 5
y = 10
x, y = y, x
print(x,y)
# 10,5
# No temporary variable needed.

# * Dynamic Typing:
x = 10
x = "hello"
print(x)
#? Same variable, different type.
# Python allows it.
#? behind work:basic but u should know
# x  ───►  10  (int object)
# x = "hello" , Python does NOT change 10 into "hello".
# Instead:
# A new object "hello" (class str) is created
# x now points to this new object
# The old object 10 loses one reference
# now memeory looks like:
# x  ───►  "hello"  (str object)
# 10  (may be garbage collected if no reference left)
# *Checking Identity

x = 10
y = 10
print(x is y)
# is checks if both refer to the same object.
# output:true