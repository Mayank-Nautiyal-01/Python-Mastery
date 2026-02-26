
#! Strings (Deep dive)
# ?string is an immutable sequence of Unicode characters.

# ? 1> Creating Strings:
s1 = "hello"
s2 = 'world'
s3 = """multi
line
string"""
# All are str type.

#? 2>Strings Are Immutable
# You cannot change characters directly.
s = "hello"
s[0] = "H"   #  TypeError

# Why?
# Because string objects cannot be modified after creation.
# Correct way:

s = "hello"
s = "H" + s[1:] # s[1:]:What is this ?,Start from index 1,Go till end
print(s)  # Hello
# New object created.

# ? 3>>Indexing:
text = "Python"

# Index mapping:

#  P  y  t  h  o  n
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1

# Ex:
print(text[0])   # P
print(text[-1])  # n

# ? 4>Slicing
# Syntax:
# string[start:end:step]

#* start included
# end excluded
# step controls jump direction

# If step is negative:

#* slicing goes backward
# start defaults to last index
# end defaults to before first index

text = "Python"
# P  y  t  h  o  n
# 0  1  2  3  4  5

print(text[0:4])   # start=0, end=4 (excluded) → indices 0,1,2,3 → "Pyth"
print(text[:3])    # start omitted (=0), end=3 → indices 0,1,2 → "Pyt"
print(text[3:])    # start=3, end omitted (=len) → indices 3,4,5 → "hon"
print(text[::2])   # start=0, end=6, step=2 → indices 0,2,4 → "Pto"
# Explanation:
# Start at 0 → P
# Jump 2 → index 2 → t
# Jump 2 → index 4 → o
print(text[::-1])  # start=end, step=-1 → reverse → "nohtyP"
# Explanation:
# Step = -1 → move backward
# Default start becomes last index (5)
# Default end becomes before index -1
# So it walks: 5,4,3,2,1,0

# ?String Methods (Very Important):

# *Case methods:
s = "hello World"

print(s.upper())     # HELLO WORLD
print(s.lower())     # hello world
print(s.title())     # Hello World
print(s.capitalize())# Hello world

# *Check methods:
print("abc".isalpha())   # True
print("123".isdigit())   # True
print("abc123".isalnum())# True,isalnum() = is alphanumeric
print("   ".isspace())   # True

# *Strip methods
s = "  hello  "

print(s.strip())   # "hello"
print(s.lstrip())  # "hello ",Removes whitespace from left side only.
print(s.rstrip())  # " hello",Removes whitespace from RIGHT side only.

# *Replace:

s = "I like Java"
print(s.replace("Java", "Python")) #I like Python

# *Split:
data = "apple,banana,mango"
print(data.split(","))  
# ['apple', 'banana', 'mango']

# *Join (Very Important):
words = ["I", "love", "Python"]
print(" ".join(words))

# ?6>Membership:
print("Py" in "Python")  # True
print("py" in "Python")  # False (case-sensitive)

# Strings are case-sensitive.

#? 7> String Formatting
# f-strings (Best)
name = "Mayank"
print(f"My name is {name}")

# You can even compute inside:
print(f"2 + 3 = {2 + 3}")

# * 8>Escape Characters
print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Hi\"")

# Common escapes:
# \n → new line
# \t → tab
# \\ → backslash
# \" → double quote