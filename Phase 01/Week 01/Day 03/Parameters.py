print("=====================================================")
print("          PYTHON PARAMETERS CHEAT SHEET              ")
print("=====================================================")

# ---------------------------------------------------------
# Vocabulary Check: Parameter vs. Argument
# ---------------------------------------------------------
# PARAMETER: The variable listed inside the parentheses in the function definition.
# ARGUMENT: The actual value that is sent to the function when it is called.

# ---------------------------------------------------------
# 1. Positional Arguments (The Standard Way)
# ---------------------------------------------------------
print("\n--- 1. Positional Arguments ---")
print("Order matters! The first argument goes to the first parameter.")

def create_profile(name, age, role):
    print(f"Profile created: {name}, {age} years old, works as {role}.")

# "Sam" goes to 'name', 25 goes to 'age', "Admin" goes to 'role'
create_profile("Sam", 25, "Admin")


# ---------------------------------------------------------
# 2. Keyword Arguments
# ---------------------------------------------------------
print("\n--- 2. Keyword Arguments ---")
print("You explicitly name the parameters, so order no longer matters.")

# We can call the exact same function from above, but mix up the order
create_profile(role="Developer", name="Zoe", age=28)


# ---------------------------------------------------------
# 3. Default Parameters (Making arguments optional)
# ---------------------------------------------------------
print("\n--- 3. Default Parameters ---")
print("Provide a fallback value in case the user doesn't provide one.")

def book_flight(destination, class_type="Economy"):
    print(f"Booking flight to {destination} in {class_type} class.")

book_flight("Japan", "Business")  # Overrides the default
book_flight("Australia")          # Falls back to "Economy"


# ---------------------------------------------------------
# 4. Arbitrary Arguments (*args)
# ---------------------------------------------------------
print("\n--- 4. Arbitrary Arguments (*args) ---")
print("Use * when you don't know how many positional arguments will be passed.")
print("Python packs them all into a TUPLE.")

def make_pizza(size, *toppings):
    print(f"\nMaking a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

make_pizza("Large", "Pepperoni", "Mushrooms", "Extra Cheese")
make_pizza("Small", "Just Cheese")


# ---------------------------------------------------------
# 5. Arbitrary Keyword Arguments (**kwargs)
# ---------------------------------------------------------
print("\n--- 5. Arbitrary Keyword Arguments (**kwargs) ---")
print("Use ** when you don't know how many keyword arguments will be passed.")
print("Python packs them all into a DICTIONARY.")

def build_user_profile(first, last, **user_info):
    # We start by building a standard dictionary
    profile = {"first_name": first, "last_name": last}
    # Then we merge in whatever extra info the user provided
    profile.update(user_info)
    return profile

user1 = build_user_profile("Albert", "Einstein", field="Physics", location="Princeton")
user2 = build_user_profile("Marie", "Curie", field="Chemistry", awards=2)

print(f"User 1: {user1}")
print(f"User 2: {user2}")


# ---------------------------------------------------------
# 6. THE GOLDEN RULE OF PARAMETER ORDER
# ---------------------------------------------------------
print("\n--- 6. The Golden Rule of Parameter Ordering ---")
print("If you mix different types of parameters, they MUST go in this exact order:")
print("1. Standard Positional Parameters")
print("2. *args")
print("3. Default Parameters")
print("4. **kwargs")

def ultimate_function(a, b, *args, default_param="Hello", **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"default_param: {default_param}")
    print(f"kwargs: {kwargs}")

# Let's test the ultimate function!
print("\nCalling ultimate_function(1, 2, 3, 4, 5, default_param='Hi', x=99, y=100):")
ultimate_function(1, 2, 3, 4, 5, default_param="Hi", x=99, y=100)

print("\n=====================================================")