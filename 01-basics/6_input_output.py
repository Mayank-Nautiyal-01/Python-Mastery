
# !Input / Output 

# Input = taking data from user
# Output = displaying data to user

# ? 1️ Output → print()



print("Hello World")

# You can print multiple values:

# name = "Mayank"
# age = 21
# print(name, age)

# Output:Mayank 21

# * sep parameter=Controls separator between values.

print("Mayank", 21, sep="-")

# Output:Mayank-21

# * end parameter:Controls what happens at the end.

print("Hello", end=" ")
print("World")

# Output:Hello World

# Default end is \n (new line).

#  ?2️ Input → input()=

# Basic:
# name = input("Enter your name: ")
# print("Hello", name)

# note:==
# input() ALWAYS returns a string.
# Even if user types number.

age = input("Enter age: ")
print(type(age))

# Output:<class 'str'>

#  Why This Matters
# This will break:

# age = input("Enter age: ")
# print(age + 5)
# Because:
# "21" + 5 ❌

# You must convert:
# age = int(input("Enter age: "))
# print(age + 5)


# ? 3️ Multiple Inputs in One Line==
a, b = input("Enter two numbers: ").split()
# This gives strings.
# Convert properly:

a, b = map(int, input().split())


#?  4️ Formatted Output (Important):

#  f-strings (Best way)
name = "Mayank"
age = 21

print(f"My name is {name} and I am {age} years old.")


#  format()-older way
print("My name is {} and I am {} years old.".format(name, age))


# ans this ques

# What will this print?

x = input("Enter number: ")
print(x * 3)

# If user enters:
5