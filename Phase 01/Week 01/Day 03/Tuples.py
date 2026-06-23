print("=====================================================")
print("             PYTHON TUPLES CHEAT SHEET               ")
print("=====================================================")

# ---------------------------------------------------------
# 1. Creating Tuples & Key Characteristics
# ---------------------------------------------------------
print("\n--- 1. Creating Tuples ---")
print("Tuples use parentheses () instead of square brackets [].")
print("They are ordered, unchangeable (immutable), and allow duplicates.")

coordinates = (10, 20, 30)
mixed_tuple = ("Alice", 25, True, "Alice")

print(f"Coordinates Tuple: {coordinates}")
print(f"Mixed Tuple      : {mixed_tuple}")

# CRITICAL QUIRK: Creating a tuple with only ONE item
# You MUST include a trailing comma, otherwise Python thinks it's just a string/math expression!
not_a_tuple = ("apple")
real_tuple = ("apple",)
print(f"\nType of ('apple')  : {type(not_a_tuple)}")
print(f"Type of ('apple',) : {type(real_tuple)}")


# ---------------------------------------------------------
# 2. Accessing Items (Just like Lists)
# ---------------------------------------------------------
print("\n--- 2. Accessing Items ---")
print("Indexing and slicing work exactly the same as they do with lists.")

fruits = ("apple", "banana", "cherry", "orange", "kiwi")

print(f"fruits[0] (First)   : {fruits[0]}")
print(f"fruits[-1] (Last)   : {fruits[-1]}")
print(f"fruits[1:4] (Slice) : {fruits[1:4]}")


# ---------------------------------------------------------
# 3. The Golden Rule: Immutability
# ---------------------------------------------------------
print("\n--- 3. The Golden Rule: Immutability ---")
print("You CANNOT change, add, or remove items after a tuple is created.")

# coordinates[0] = 99  <-- THIS WILL CRASH YOUR PROGRAM (TypeError)

print("Workaround: If you MUST change a tuple, convert it to a list first, change it, then convert back.")
temp_list = list(coordinates)
temp_list[0] = 99
new_coordinates = tuple(temp_list)

print(f"Original coordinates : {coordinates}")
print(f"New coordinates      : {new_coordinates}")


# ---------------------------------------------------------
# 4. Unpacking Tuples (Extremely Useful!)
# ---------------------------------------------------------
print("\n--- 4. Unpacking Tuples ---")
print("You can extract tuple values directly into variables.")

person = ("John", 30, "Engineer")

# The number of variables must match the number of items in the tuple!
name, age, profession = person

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")

# What if you have too many items? Use the asterisk (*) to grab the rest as a list!
colors = ("red", "green", "blue", "yellow", "purple")
primary, secondary, *others = colors

print(f"\nPrimary   : {primary}")
print(f"Secondary : {secondary}")
print(f"Others    : {others} (Notice this becomes a list!)")


# ---------------------------------------------------------
# 5. Tuple Methods
# ---------------------------------------------------------
print("\n--- 5. Tuple Methods ---")
print("Because tuples are unchangeable, they only have TWO built-in methods.")

numbers = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 7)
print(f"Tuple data: {numbers}")

# count() -> Returns the number of times a specified value appears
sevens = numbers.count(7)
print(f"numbers.count(7) : {sevens} times")

# index() -> Searches the tuple for a specified value and returns its FIRST position
first_eight = numbers.index(8)
print(f"numbers.index(8) : Found at index {first_eight}")

print("\n=====================================================")