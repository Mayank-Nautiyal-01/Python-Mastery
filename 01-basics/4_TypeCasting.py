
# ! Type casting means:Converting one data type into another data type.

#? Why Type Casting Is Needed

age=input("enter age:")
print(age+5)

# ?This will throw an error.
#? why? Because input() always returns a string.
# * so "21"+ 5 which defiently give error coz there have diff type
# ? sol: 
age=int(input("enter age"))
print(age+5)
#  age:5 ,output:10

# !Common Type Casting Functions:

#? 1> int():
a= int("10")
print(a)
# int typecast it from string to integer but:
# * It works only if the string:
# Contains digits
# Optionally has a sign (+/-)
# so output: 10

b=int(5.8)
print(b)
# output:5

int("hello")
# output:valueError
# *Python tries to interpret the string "hello" as a number.It contains letters,It has no numeric meaning etc.

# ? 2>float()
float("3.14")   # 3.14
float(10)       # 10.0

# ?3>str()
str(10)       # "10"
str(3.14)     # "3.14"

# ?4>bool()
bool(1)       # True
bool(0)       # False
bool("")      # False
bool("hi")    # True
bool([])      # False
bool([1])     # True
# Rule:
# Empty → False
# Zero → False
# Everything else → True

# ?----------------------------

#! Implicit vs Explicit Casting:

#?Implicit (Automatic):
 
x = 5
y = 2.0
print(x + y)
# 7.0
# Python automatically converts int to float.

# ?Explicit (Manual):

x = "10"
y = int(x)
print(y)
# 10

# ?------------------
# Important Understanding:
# Type casting does NOT change the original object.

x = "10"
y = int(x)

print(x)
print(y)
print(type(x))
print(type(y))

# 10
# 10
# <class 'str'>
# <class 'int'>

# *Now observe carefully:
# x is still a string
# y is a new integer object
# Nothing about x changed.