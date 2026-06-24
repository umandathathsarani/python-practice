print("=====================================================")
print("          PYTHON RETURN STATEMENT CHEAT SHEET        ")
print("=====================================================")

# ---------------------------------------------------------
# 1. Basic Return Statement
# ---------------------------------------------------------
print("\n--- 1. Basic Return ---")
print("Return hands a value back to the caller.")

def calculate_square(number):
    result = number * number
    return result  # The function ends here and gives back 'result'

# We capture the returned value by assigning it to a variable
my_square = calculate_square(5)
print(f"The returned square is: {my_square}")


# ---------------------------------------------------------
# 2. Print vs. Return (The Crucial Difference)
# ---------------------------------------------------------
print("\n--- 2. Print vs. Return ---")

def just_print(a, b):
    print(f"I am just printing: {a + b}")
    # No return statement here!

def actually_return(a, b):
    return a + b

# Let's try to save the results of both:
print_result = just_print(10, 5)
return_result = actually_return(10, 5)

print(f"Value stored from just_print()   : {print_result} (Because it didn't return anything!)")
print(f"Value stored from actually_return(): {return_result} (Now we can do math with this!)")


# ---------------------------------------------------------
# 3. Returning Multiple Values (Tuple Magic!)
# ---------------------------------------------------------
print("\n--- 3. Returning Multiple Values ---")
print("Python allows you to return multiple values separated by commas.")
print("It secretly packages them into a TUPLE, which you can unpack!")

def get_user_stats():
    name = "Amal"
    score = 95
    level = 5
    return name, score, level  # Returning 3 things at once!

# Unpacking the returned tuple directly into variables (Just like you learned earlier!)
user_name, user_score, user_level = get_user_stats()

print(f"Name: {user_name}, Score: {user_score}, Level: {user_level}")


# ---------------------------------------------------------
# 4. Early Returns (Using Return to Stop a Function)
# ---------------------------------------------------------
print("\n--- 4. Early Returns ---")
print("As soon as Python hits a 'return' statement, the function immediately stops.")

def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero!"  # The function instantly stops here if num2 is 0
    
    # This line only runs if the early return wasn't triggered
    return num1 / num2

print(f"10 divided by 2: {divide_numbers(10, 2)}")
print(f"10 divided by 0: {divide_numbers(10, 0)}")


# ---------------------------------------------------------
# 5. What happens if you don't use return?
# ---------------------------------------------------------
print("\n--- 5. The Default Return Value ---")
print("If a function finishes without hitting a return statement, it returns 'None'.")

def say_hello():
    greeting = "Hello there!"
    # I forgot to return the greeting!

result = say_hello()
print(f"The result of say_hello() is: {result}")

print("\n=====================================================")