print("=====================================================")
print("            PYTHON FUNCTIONS CHEAT SHEET             ")
print("=====================================================")

# ---------------------------------------------------------
# 1. Defining and Calling a Basic Function
# ---------------------------------------------------------
print("\n--- 1. Basic Functions ---")
print("Use the 'def' keyword to create a function.")

def say_hello():
    print("Hello! Welcome to Day 03.")

# The function won't do anything until you 'call' it:
say_hello()


# ---------------------------------------------------------
# 2. Parameters and Arguments
# ---------------------------------------------------------
print("\n--- 2. Parameters & Arguments ---")
print("Passing data into a function to make it dynamic.")

# 'name' is the parameter (the variable inside the definition)
def greet_user(name):
    print(f"Good morning, {name}!")

# "Amal" is the argument (the actual data we pass in)
greet_user("Amal")
greet_user("Kamal")


# ---------------------------------------------------------
# 3. The Return Statement
# ---------------------------------------------------------
print("\n--- 3. Return Statements ---")
print("Returning data back to the caller instead of just printing it.")

def add_numbers(num1, num2):
    result = num1 + num2
    return result  # Hands the value back to wherever the function was called

# We capture the returned value in a variable
total = add_numbers(10, 15)
print(f"The returned total is: {total}")


# ---------------------------------------------------------
# 4. Keyword Arguments
# ---------------------------------------------------------
print("\n--- 4. Keyword Arguments ---")
print("You can explicitly state which parameter gets which value.")

def calculate_total(price, tax):
    return price + (price * tax)

# Normal positional arguments (order matters)
print(f"Positional : {calculate_total(100, 0.05)}")

# Keyword arguments (order DOES NOT matter)
print(f"Keyword    : {calculate_total(tax=0.05, price=100)}")


# ---------------------------------------------------------
# 5. Default Parameters
# ---------------------------------------------------------
print("\n--- 5. Default Parameters ---")
print("Giving a parameter a default value if the user forgets to provide one.")

def order_coffee(size="Medium"):
    print(f"Preparing a {size} coffee.")

order_coffee("Large")  # Overrides the default
order_coffee()         # Falls back to "Medium"


# ---------------------------------------------------------
# 6. Advanced: Flexible Arguments (*args)
# ---------------------------------------------------------
print("\n--- 6. Flexible Arguments (*args) ---")
print("What if you don't know how many arguments will be passed? Use *args!")
print("*args gathers all positional arguments into a TUPLE.")

def multiply_all(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

print(f"Multiplying 2, 3, 4 : {multiply_all(2, 3, 4)}")
print(f"Multiplying 5, 10   : {multiply_all(5, 10)}")


# ---------------------------------------------------------
# 7. Advanced: Flexible Keyword Arguments (**kwargs)
# ---------------------------------------------------------
print("\n--- 7. Flexible Keyword Arguments (**kwargs) ---")
print("**kwargs gathers any unknown keyword arguments into a DICTIONARY.")

def display_user_info(**details):
    # 'details' is now a dictionary
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

# We can pass as many custom keyword arguments as we want
display_user_info(name="Zoe", age=22, location="Canada", major="IT")

print("\n=====================================================")