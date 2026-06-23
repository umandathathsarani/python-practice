print("=====================================================")
print("        PYTHON UNPACKING MASTER CHEAT SHEET          ")
print("=====================================================")

# ---------------------------------------------------------
# 1. Basic Iterable Unpacking
# ---------------------------------------------------------
print("\n--- 1. Basic Iterable Unpacking ---")

# Unpacking a tuple
coordinates = (40.7128, -74.0060)
lat, lon = coordinates
print(f"Tuple Unpacked -> Lat: {lat}, Lon: {lon}")

# Unpacking a list
user = ["Alice", "Admin", 30]
name, role, age = user
print(f"List Unpacked  -> Name: {name}, Role: {role}, Age: {age}")

# Error Warning: If variable count doesn't match item count exactly, you get a ValueError.


# ---------------------------------------------------------
# 2. Extended Unpacking with the Star (*) Operator
# ---------------------------------------------------------
print("\n--- 2. Extended Unpacking (Star Operator) ---")

# Gather Remaining Elements
scores = [95, 88, 72, 64, 50]
highest, second, *the_rest = scores
print(f"Highest: {highest}")
print(f"The Rest (List): {the_rest}")

# Gather Middle Elements
items = ["TokenA", 100, 200, 300, "Active"]
header, *data, status = items
print(f"\nHeader: {header}, Status: {status}")
print(f"Middle Data: {data}")

# Ignoring Values with Underscores
# Only grab the first and last element
first, *_, last = [1, 2, 3, 4, 5]
print(f"\nFirst: {first}, Last: {last} (Middle was ignored)")


# ---------------------------------------------------------
# 3. Function Argument Unpacking
# ---------------------------------------------------------
print("\n--- 3. Function Argument Unpacking ---")

def setup_profile(username, access_level, status):
    print(f"User {username} is an {access_level} and is {status}.")

# * Operator: Unpacks iterables into positional arguments
user_data = ["Bob", "Editor", "Active"]
print("Using * for lists: ", end="")
setup_profile(*user_data)

# ** Operator: Unpacks dictionaries into keyword arguments
user_dict = {"username": "Sara", "access_level": "Admin", "status": "Inactive"}
print("Using ** for dicts: ", end="")
setup_profile(**user_dict)


# ---------------------------------------------------------
# 4. Merging Collections
# ---------------------------------------------------------
print("\n--- 4. Merging Collections ---")

# Merging Lists or Tuples
list_a = [1, 2]
list_b = [3, 4]
combined_list = [*list_a, *list_b, 5]
print(f"Merged Lists: {combined_list}")

# Merging Dictionaries
# If keys overlap, the last unpacked dictionary overwrites previous values.
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 99, "z": 3}
merged_dict = {**dict_a, **dict_b}
print(f"Merged Dicts: {merged_dict}")


# ---------------------------------------------------------
# 5. Loop and Nested Unpacking
# ---------------------------------------------------------
print("\n--- 5. Loop and Nested Unpacking ---")

# In For Loops
pricing = {"Apple": 0.99, "Banana": 0.59}
print("Looping through dictionary items:")
for product, price in pricing.items():
    print(f"  {product} costs ${price}")

# Nested Unpacking (Matching structure perfectly)
print("\nNested Unpacking:")
nested_data = ("Employee", ("John", "Doe"))

# The variables on the left match the shape of the data on the right
role, (first_name, last_name) = nested_data

print(f"Role: {role}, First Name: {first_name}, Last Name: {last_name}")

print("\n=====================================================")