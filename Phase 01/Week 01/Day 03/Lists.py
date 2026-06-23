print("=====================================================")
print("            PYTHON LISTS CHEAT SHEET                 ")
print("=====================================================")

# ---------------------------------------------------------
# Creating Lists & Key Characteristics
# ---------------------------------------------------------
print("\n--- 1. Creating Lists ---")
print("Lists are built-in, mutable, ordered, allow duplicates, and can be heterogeneous.")

fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", True, 3.14, ["nested", "list"]]

print(f"Basic List: {fruits}")
print(f"Mixed Data Type List: {mixed_list}")


# ---------------------------------------------------------
# Accessing Items (Indexing)
# ---------------------------------------------------------
print("\n--- 2. Accessing Items ---")
print("Python uses zero-based indexing. Negative indexing reads from the right.")

print(f"List: {fruits}")
print(f"fruits[0] (First item) : {fruits[0]}")
print(f"fruits[-1] (Last item) : {fruits[-1]}")


# ---------------------------------------------------------
# Adding Items
# ---------------------------------------------------------
print("\n--- 3. Adding Items ---")
numbers = [1, 2, 3]
print(f"Original: {numbers}")

numbers.append(4)               # Adds to the very end
print(f"After append(4): {numbers}")

numbers.insert(1, 99)           # Inserts 99 at index 1
print(f"After insert(1, 99): {numbers}")

numbers.extend([5, 6])          # Combines another list
print(f"After extend([5, 6]): {numbers}")


# ---------------------------------------------------------
# Removing Items
# ---------------------------------------------------------
print("\n--- 4. Removing Items ---")
items = ["mat", "bat", "hat", "cat", "bat"]
print(f"Original: {items}")

items.remove("bat")             # Deletes the *first* occurrence of "bat"
print(f"After remove('bat'): {items}")

popped_item = items.pop()       # Removes and returns the LAST item (default)
print(f"After pop() [removed '{popped_item}']: {items}")

items.pop(0)                    # Removes the item at index 0 ("mat")
print(f"After pop(0): {items}")

items.clear()                   # Empties the entire list
print(f"After clear(): {items}")


# ---------------------------------------------------------
# Slicing Lists [start : end : step]
# ---------------------------------------------------------
print("\n--- 5. Slicing Lists ---")
letters = ["a", "b", "c", "d", "e"]
print(f"Original: {letters}")

print(f"letters[1:4]     : {letters[1:4]} (Index 4 is excluded)")
print(f"letters[:3]      : {letters[:3]} (From start up to index 3)")
print(f"letters[2:]      : {letters[2:]} (From index 2 to the end)")
print(f"letters[::-1]    : {letters[::-1]} (Reverses the list)")


# ---------------------------------------------------------
# Essential List Methods Reference
# ---------------------------------------------------------
print("\n--- 6. Essential List Methods ---")
data = [40, 10, 30, 10, 20]
print(f"Original Data: {data}")

print(f"len(data)        : {len(data)} (Total count of elements)")

print(f"data.count(10)   : {data.count(10)} (How many times 10 appears)")

print(f"data.index(30)   : {data.index(30)} (The index position of 30)")

data.sort()                     # Sorts ascending by default
print(f"After data.sort(): {data}")

data.reverse()                  # Inverts order
print(f"After data.reverse(): {data}")


# ---------------------------------------------------------
# Extra Crucial Concepts
# ---------------------------------------------------------
print("\n--- 7. Extra Crucial List Operations ---")

# 1. Checking if an item exists (The 'in' operator)
inventory = ["sword", "shield", "potion"]
if "potion" in inventory:
    print("Yes, you have a potion!")

# 2. Copying a list properly
# (If you just do list2 = list1, they share the same memory. Changing one changes both!)
original = [1, 2, 3]
safe_copy = original.copy()
safe_copy[0] = 99
print(f"Original remains safe: {original}, while copy changed: {safe_copy}")

# 3. Quick Math on Lists
nums = [5, 10, 15]
print(f"Sum of list: {sum(nums)}, Max: {max(nums)}, Min: {min(nums)}")


# ---------------------------------------------------------
# Advanced: List Comprehension
# ---------------------------------------------------------
print("\n--- 8. Advanced: List Comprehension ---")
print("A shorthand syntax to construct new lists from existing iterables.")

# Traditional way
squares_traditional = []
for x in range(5):
    squares_traditional.append(x**2)
print(f"Traditional loop: {squares_traditional}")

# Shorthand List Comprehension
squares_comp = [x**2 for x in range(5)]
print(f"List Comprehension: {squares_comp}")

# You can even add 'if' conditions inside them! (e.g., only even numbers)
evens = [x for x in range(10) if x % 2 == 0]
print(f"Comprehension with IF condition (Evens 0-9): {evens}")

print("\n=====================================================")