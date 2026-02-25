
# ! Operators are symbols that perform operations on values and variables.

# ?Arithmetic Operators::
# Used for mathematical calculations.

a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...,/ → always returns float
print(a // b)  # 3  (floor division),// → removes decimal part (floor)
print(a % b)   # 1  (remainder)
print(a ** b)  # 1000 (power)

# ?Comparison Operators::
# Used to compare values. Return boolean.

print(5 > 3)     # True
print(5 < 3)     # False
print(5 == 5)    # True
print(5 != 5)    # False
print(5 >= 5)    # True
print(5 <= 3)    # False

# Remember:
# == checks value
# = is assignment

# ?Comparison Operators::
# Used to compare values. Return boolean.

print(5 > 3)     # True
print(5 < 3)     # False
print(5 == 5)    # True
print(5 != 5)    # False
print(5 >= 5)    # True
print(5 <= 3)    # False

# Remember:
# == checks value
# = is assignment

#?Assignment Operators:: too basic 
x = 5
x += 3   # x = x + 3
x -= 2
x *= 4
x /= 2
x %= 3
x **= 2

#? Identity Operators::
# Check memory identity.

a = [1,2]
b = a
c = [1,2]

print(a is b)  # True
print(a is c)  # False

# diff b/w is and ==
# is → checks memory
# == → checks value

# ?Membership Operators::
print(2 in [1,2,3])     # True
print(5 not in [1,2,3]) # True

# Works for:
# list
# tuple
# set
# string
# dict (checks keys)

# Bitwise Operators (Advanced but important)
print(5 & 3)  # AND
print(5 | 3)  # OR
print(5 ^ 3)  # XOR
print(~5)     # NOT
print(5 << 1) # Left shift
print(5 >> 1) # Right shift

# ==lets see bitwise little more how it will works"
# *Convert to Binary First=
# 5  = 0101
# 3  = 0011
# (We use 4 bits here for simplicity.)

#? 1> & (AND):

# Rule:
# 1 & 1 = 1
# Anything else = 0
# Now apply:

#   0101   (5)
# & 0011   (3)
# --------
#   0001

# Binary 0001 = 1
# print(5 & 3)  # 1

#? 2> & (AND)

# Rule:
# 1 & 1 = 1
# Anything else = 0
# Now apply:

#   0101   (5)
# & 0011   (3)
# --------
#   0001

# Binary 0001 = 1
# print(5 & 3)  # 1

#? 3> ^ (XOR – Exclusive OR)
# Rule:

# 1 if bits are different
# 0 if bits are same
#   0101
# ^ 0011
# --------
#   0110

# Binary 0110 = 6
# print(5 ^ 3)  # 6

# ?4> ~ (NOT / Bitwise Complement)

# This flips all bits.
# But here’s the tricky part.
# Python uses two’s complement representation.
# Formula shortcut:

# ~x = -(x + 1)

# So:
# ~5 = -(5 + 1)
#      = -6
# print(~5)  # -6

#? 5 << (Left Shift)

# Shifts bits to the left.
# Adds zeros on right.
# 5 = 0101

# Shift left by 1:
# 1010
# Binary 1010 = 10

# Shortcut formula:
# x << n = x * (2^n)
# So:
# 5 << 1 = 5 * 2 = 10

# ? 6 >> (Right Shift)

# Shifts bits to the right.
# 0101
# Shift right by 1:
# 0010
# Binary 0010 = 2
# Shortcut formula:

# x >> n = x // (2^n)
# So:
# 5 >> 1 = 5 // 2 = 2