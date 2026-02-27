# ==========================================
# PYTHON CONDITIONAL STATEMENTS
# ==========================================
# Conditional statements allow decision making.
# Code runs based on whether a condition is True or False.
# The primary keywords are: `if`, `elif` (else if), and `else`.

# ---------------------------------------------------------
# 1. The Simple 'if' Statement
# ---------------------------------------------------------
# The 'if' statement evaluates a condition (a boolean expression that results in True or False).
# If the condition is True, the indented block of code right below it will execute.

age = 18


if age >= 18:
    # Notice the indentation! Python uses indentation to define code blocks, we discuss it earlier topic when there is a indentation error comes check that too
    # This print statement only runs because 18 is greater than or equal to 18 (True).
    print("You are eligible to vote.")

# ---------------------------------------------------------
# 2. The 'if-else' Statement
# ---------------------------------------------------------
# What if the condition is False? We can use 'else' to provide an alternative block of code.
# It translates to: "If this is true, do X. Otherwise, do Y."

temperature = 15


if temperature > 25:
    print("It's a hot day. Wear shorts!")
else:
    # Since 15 is NOT greater than 25, the 'if' condition is False.
    # Therefore, the execution jumps to this 'else' block.
    print("It's not that hot. Bring a jacket.")

# ---------------------------------------------------------
# 3. The 'if-elif-else' Statement (Multiple Conditions)
# ---------------------------------------------------------
# Sometimes you have more than two possibilities. That's where 'elif' (short for else if) comes in.
# Python checks each condition one by one from top to bottom.
# As soon as it finds a True condition, it executes that block and skips the rest.

marks = 85


if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    # 85 is not >= 90, so the first condition is False.
    # But 85 IS >= 80, so this condition is True! This block runs.
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    # If none of the above conditions are True, the 'else' block serves as a catch-all.
    print("Grade: Do better next time.")

# ---------------------------------------------------------
# 4. Nested 'if' Statements
# ---------------------------------------------------------
# You can put an 'if' statement inside another 'if' statement!
# This is useful when you need to check a condition only after another condition has proven True.

has_ticket = True
is_vip = False


if has_ticket:
    print("You can enter the concert.")
    
    # This inner 'if' is only checked because has_ticket is True.
    if is_vip:
        print("Welcome to the VIP lounge!")
    else:
        print("Please proceed to the general admission area.")
else:
    print("You cannot enter without a ticket.")

# ---------------------------------------------------------
# 5. Logical Operators (and, or, not) with Conditionals
# ---------------------------------------------------------
# You can combine multiple conditions into a single 'if' statement using logical operators.

is_weekend = True
is_sunny = True


# 'and' means BOTH conditions must be True.
if is_weekend and is_sunny:
    print("Perfect weather for a picnic!")

# 'or' means AT LEAST ONE condition must be True.
has_cash = False
has_card = True

if has_cash or has_card:
    print("You can buy the groceries.")

# 'not' reverses the boolean value (True becomes False, False becomes True).
is_raining = False

if not is_raining:
    print("You don't need an umbrella.")

# ---------------------------------------------------------
# 6. The Ternary Operator (Conditional Expression)
# ---------------------------------------------------------
# A shorter way to write a simple if-else on a single line.
# Syntax: [value_if_true] if [condition] else [value_if_false]

number = 7


result = "Even" if number % 2 == 0 else "Odd"
# Since 7 % 2 is not 0 (False), it picks the value after 'else' -> "Odd".
print(f"The number {number} is {result}.")

# ---------------------------------------------------------
# 7. Match-Case (Available in Python 3.10+)
# ---------------------------------------------------------
# Match-Case is similar to the 'switch' statement in other languages.
# It is excellent for checking a variable against multiple specific values.

status_code = 404


match status_code:
    case 200:
        print("Success: Everything is OK!")
    case 404:
        print("Error: Not Found. Check your URL.")
    case 500:
        print("Error: Internal Server Error.")
    case _:
        # The underscore '_' is essentially the 'else' case here.
        # It catches everything that wasn't specifically handled above.
        print("Unknown status code.")

