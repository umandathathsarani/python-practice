print("=====================================================")
print("     PYTHON DICTIONARIES MASTER CHEAT SHEET          ")
print("=====================================================")

# ---------------------------------------------------------
# Core Characteristics (The Theory)
# ---------------------------------------------------------
print("\n--- Core Characteristics ---")
print("- Keys: MUST be unique and immutable (strings, numbers, tuples).")
print("- Values: Can be absolutely anything (even other lists/dicts), and can repeat.")
print("- Ordered: Since Python 3.7, they remember the order you added items.")
print("- Fast: They use hash tables, making lookups incredibly fast (O(1) average).")


# ---------------------------------------------------------
# 1. Creating Dictionaries
# ---------------------------------------------------------
print("\n--- 1. Creating a Dictionary ---")

# Method A: Using curly braces (Literal syntax - Most Common)
user_profile = {
    "username": "coder123",
    "score": 95,
    "verified": True
}
print(f"Literal Syntax : {user_profile}")

# Method B: Using the dict() constructor
empty_dict = dict()
setup_dict = dict(brand="Ford", model="Mustang", year=1964)
print(f"dict() Syntax  : {setup_dict}")


# ---------------------------------------------------------
# 2. Accessing Items
# ---------------------------------------------------------
print("\n--- 2. Accessing Items ---")

# Square brackets method (Throws a KeyError if missing)
print(f"Username (using [])  : {user_profile['username']}")

# Safe Lookup with .get() (Returns None if missing)
print(f"Email (using .get()) : {user_profile.get('email')}")

# Safe Lookup with a custom default fallback ("N/A")
print(f"Email (with default) : {user_profile.get('email', 'N/A')}")


# ---------------------------------------------------------
# 3. Adding and Updating Items
# ---------------------------------------------------------
print("\n--- 3. Adding and Updating Items ---")

# Assigning a value to a key creates it if missing, or overwrites if it exists
user_profile["email"] = "user@example.com"  # Adds new pair
user_profile["score"] = 100                 # Updates existing value

print(f"After Add/Update: {user_profile}")


# ---------------------------------------------------------
# 4. Removing Items
# ---------------------------------------------------------
print("\n--- 4. Removing Items ---")

# del -> Removes specific key entirely
del user_profile["verified"]
print(f"After 'del'            : {user_profile}")

# .pop() -> Removes specific key AND returns its value
removed_score = user_profile.pop("score")
print(f"After .pop('score')    : {user_profile} (Returned: {removed_score})")

# .popitem() -> Removes and returns the last inserted key-value pair
last_item = user_profile.popitem()
print(f"After .popitem()       : {user_profile} (Returned: {last_item})")


# ---------------------------------------------------------
# 5. Iterating Through Dictionaries
# ---------------------------------------------------------
print("\n--- 5. Iterating Through Dictionaries ---")
inventory = {"apples": 10, "bananas": 5, "oranges": 8}

print("Looping through keys only:")
for fruit in inventory:
    print(f" - {fruit}")

print("\nLooping through values only:")
for count in inventory.values():
    print(f" - Quantity: {count}")

print("\nLooping through BOTH (simultaneously):")
for fruit, count in inventory.items():
    print(f" - Fruit: {fruit}, Quantity: {count}")


# ---------------------------------------------------------
# Common Built-In Methods Reference
# ---------------------------------------------------------
print("\n--- Common Built-In Methods Refresher ---")
test_dict = {"a": 1, "b": 2}
print(f".keys()   -> Returns view of keys: {test_dict.keys()}")
print(f".values() -> Returns view of vals: {test_dict.values()}")
print(f".items()  -> Returns tuples      : {test_dict.items()}")

test_dict.update({"c": 3, "a": 99}) # Merges/updates data
print(f".update() -> Merged with new data: {test_dict}")

test_dict.clear()                   # Empties dictionary
print(f".clear()  -> Empties dictionary  : {test_dict}")

print("\n=====================================================")