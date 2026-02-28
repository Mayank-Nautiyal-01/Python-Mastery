# ==========================================
# PYTHON LOOPS
# ==========================================
# Loops allow you to execute a block of code multiple times.
# They are essential when you want to repeat a task without writing the same code over and over.
# The two primary types of loops in Python are: `for` and `while`.

# ---------------------------------------------------------
# 1. The 'for' Loop
# ---------------------------------------------------------
# A 'for' loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string).
# It executes a block of code for each item in the sequence.

# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]

# This loop reads: "For each fruit inside the fruits list, do something."
for fruit in fruits:
    print(fruit)

# Example 2: Iterating over a string
# We can loop through each character in a string.
word = "Python"
for char in word:
    print(char)

# ---------------------------------------------------------
# 2. The 'for' Loop with range()
# ---------------------------------------------------------
# The range() function returns a sequence of numbers.
# We often use range() with a 'for' loop when we want to run a loop a specific number of times.

# range(5) will generate numbers from 0 up to 4 (it stops BEFORE the provided number).
for i in range(5):
    print(f"Number: {i}")

# You can also specify a start, stop, and step: range(start, stop, step)
# This generates numbers starting at 2, up to (but not including) 10, jumping by 2.
for x in range(2, 10, 2):
    print(f"Even number: {x}")

# ---------------------------------------------------------
# 3. The 'while' Loop
# ---------------------------------------------------------
# A 'while' loop executes a block of code AS LONG AS a specified condition is True.
# IMPORTANT: You must ensure the condition eventually becomes False, 
# otherwise you will create an "infinite loop" that never stops!

count = 1

# This loop reads: "While count is less than or equal to 5, keep running this block."
while count <= 5:
    print(f"Count is: {count}")
    # We MUST increment the count, or the loop will run forever!
    count += 1 

# ---------------------------------------------------------
# 4. Loop Control Statements: 'break' and 'continue'
# ---------------------------------------------------------
# These keywords allow you to change the normal flow of a loop.

# --- The 'break' Statement ---
# 'break' immediately EXITS the entire loop.
print("\nTesting 'break':")
for num in range(1, 10):
    if num == 5:
        # As soon as num equals 5, the loop completely stops.
        print("Found 5, breaking out!")
        break
    print(f"Number: {num}")

# --- The 'continue' Statement ---
# 'continue' skips the REST of the current iteration and jumps to the next one.
print("\nTesting 'continue':")
for num in range(1, 6):
    if num == 3:
        # When num is 3, we skip the print statement below and jump to 4.
        continue
    print(f"Number: {num}")

# ---------------------------------------------------------
# 5. The 'else' clause in Loops
# ---------------------------------------------------------
# Both 'for' and 'while' loops can have an 'else' block.
# The 'else' block executes ONLY if the loop finishes naturally (meaning it wasn't stopped by a 'break' statement).

print("\nUsing 'else' with a loop:")
for i in range(3):
    print(i)
else:
    # This runs because the loop finished from 0 to 2 without breaking.
    print("Loop finished successfully without breaking!")

# Conversely, if we 'break', the 'else' block is skipped.
print("\nBreaking a loop with an 'else' clause:")
for i in range(3):
    if i == 1:
        print("Breaking loop at 1")
        break
    print(i)
else:
    # This will NOT run because the 'break' statement was triggered.
    print("This won't be printed.")

# ---------------------------------------------------------
# 6. Nested Loops
# ---------------------------------------------------------
# You can place a loop inside another loop! 
# The "inner loop" completes all its iterations for EACH single iteration of the "outer loop".

adj = ["red", "big"]
fruits = ["apple", "cherry"]

# For every adjective, we look at every fruit.
for a in adj:
    for f in fruits:
        print(a, f)
