# ==========================================
# PYTHON FUNCTIONS
# ==========================================
# A function is a block of organized, reusable code that is used to perform a single, related action.
# Functions provide better modularity for your application and a high degree of code reusing.

# ---------------------------------------------------------
# 1. Defining and Calling a Function
# ---------------------------------------------------------
# You define a function using the 'def' keyword.

def greet():
    """This docstring explains what the function does."""
    print("Hello from a function!")

# To "call" or execute the function, simply use its name followed by parentheses:
greet()

# ---------------------------------------------------------
# 2. Arguments (Parameters)
# ---------------------------------------------------------
# Information can be passed to functions as arguments.
# Arguments are specified after the function name, inside the parentheses.

def greet_user(name):
    # 'name' is a parameter (variable defined in the function signature)
    print(f"Hello, {name}!")

# "Alice" is the argument (the actual value passed to the function)
greet_user("Alice")
greet_user("Bob")

# ---------------------------------------------------------
# 3. Multiple Arguments and Default Values
# ---------------------------------------------------------

# You can have multiple parameters separated by commas.
# You can also set a default value. If no argument is provided, the default is used.
def describe_pet(animal_type, pet_name="Unknown"):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

# Positional arguments (order matters)
describe_pet("hamster", "Harry")

# Using the default value
describe_pet("dog")

# Keyword arguments (order doesn't matter)
describe_pet(pet_name="Willie", animal_type="dog")

# ---------------------------------------------------------
# 4. Return Values
# ---------------------------------------------------------
# A function can return a result back to the caller using the 'return' keyword.
# Once a 'return' statement is executed, the function immediately exits.

def add_numbers(x, y):
    result = x + y
    return result

# We can store the returned value in a variable
sum_result = add_numbers(5, 3)
print(f"\nThe sum is: {sum_result}")

# ---------------------------------------------------------
# 5. Functions vs. Methods
# ---------------------------------------------------------
# People often confuse "Functions" and "Methods". 
# They are very similar (both are blocks of code that perform actions), but they are called differently.

# --- FUNCTION ---
# A function is a standalone block of code. It doesn't belong to any specific object.
# You call it by its name and pass arguments to it: function_name(arguments)
print("\n--- Testing Functions vs Methods ---")
length_of_word = len("Python") # 'len()' is a built-in Python FUNCTION. It takes an argument but doesn't belong to any object.
print(f"Length of word using function: {length_of_word}")

# --- METHOD ---
# A method is a function that BELONGS to a specific object (like a string object, list object, dictionary, or a custom class).
# It's an action that a specific object can perform.
# You call it using "dot notation" directly ON the object: object.method_name(arguments)
word = "Python"
uppercase_word = word.upper() # '.upper()' is a string METHOD. It acts directly upon the 'word' string object to make it uppercase.
print(f"Uppercase word using method: {uppercase_word}")

# Another example with a list:
fruits = ["apple", "banana"]
# '.append()' is a list METHOD. It acts on the 'fruits' list object to modify it.
# We are asking the list object itself to append an item.
fruits.append("cherry") 
print(f"List after using append method: {fruits}")

# Key Difference Summary:
# - Function: Independent, passed data directly. e.g., print(data), len(data)
# - Method: Dependent on an object, called on the data itself. e.g., data.sort(), data.upper()

# ---------------------------------------------------------
# 6. Arbitrary Arguments (*args)
# ---------------------------------------------------------
# If you don't know how many arguments will be passed into your function, 
# add a * before the parameter name. The function will receive a tuple of arguments.

def make_pizza(*toppings):
    # *toppings packs all provided arguments into a single tuple named 'toppings'
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

# ---------------------------------------------------------
# 7. Arbitrary Keyword Arguments (**kwargs)
# ---------------------------------------------------------
# If you don't know how many keyword arguments will be passed,
# add two asterisks (**). The function will receive a dictionary of arguments.

def build_profile(first, last, **user_info):
    # Create an empty dictionary, then add the mandatory parameters
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    
    # Iterate over the arbitrary keyword arguments (**kwargs) and add them
    for key, value in user_info.items():
        profile[key] = value
        
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(f"\nUser Profile created with **kwargs:\n{user_profile}")
# the keyword argument here is location and field 