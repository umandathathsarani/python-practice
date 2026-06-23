print("=====================================================")
print("         PYTHON LIST METHODS MASTER CHEAT SHEET      ")
print("=====================================================")

# ---------------------------------------------------------
# 1. ADDING ITEMS TO A LIST
# ---------------------------------------------------------
print("\n--- 1. ADDING ITEMS ---")
cart = ["laptop", "mouse"]
print(f"Original cart: {cart}")

# append(item) -> Adds a single item to the END of the list
cart.append("keyboard")
print(f"1. append('keyboard')  : {cart}")

# insert(index, item) -> Inserts an item at a SPECIFIC index
cart.insert(1, "monitor")
print(f"2. insert(1, 'monitor'): {cart}")

# extend(iterable) -> Appends multiple items (from another list/tuple) to the end
extras = ["hdmi cable", "webcam"]
cart.extend(extras)
print(f"3. extend(extras)      : {cart}")


# ---------------------------------------------------------
# 2. REMOVING ITEMS FROM A LIST
# ---------------------------------------------------------
print("\n--- 2. REMOVING ITEMS ---")
colors = ["red", "blue", "green", "blue", "yellow"]
print(f"Original colors: {colors}")

# remove(item) -> Removes the FIRST occurrence of a specific value
colors.remove("blue")
print(f"1. remove('blue')      : {colors} (Notice the second blue remains)")

# pop(index) -> Removes and returns the item at the specified index. 
# If no index is specified, it removes the LAST item.
last_color = colors.pop()
print(f"2. pop()               : {colors} (Removed the last item: '{last_color}')")

index_1_color = colors.pop(1)
print(f"3. pop(1)              : {colors} (Removed index 1: '{index_1_color}')")

# clear() -> Empties the entire list
colors.clear()
print(f"4. clear()             : {colors} (List is now empty)")


# ---------------------------------------------------------
# 3. ORGANIZING & SORTING
# ---------------------------------------------------------
print("\n--- 3. ORGANIZING & SORTING ---")
scores = [85, 42, 99, 16, 73]
print(f"Original scores: {scores}")

# sort() -> Sorts the list in ascending order (modifies original list)
scores.sort()
print(f"1. sort()              : {scores}")

# sort(reverse=True) -> Sorts the list in descending order
scores.sort(reverse=True)
print(f"2. sort(reverse=True)  : {scores}")

# reverse() -> Reverses the CURRENT order of the list (does NOT sort it by value)
words = ["apple", "banana", "cherry"]
words.reverse()
print(f"3. reverse() on words  : {words}")


# ---------------------------------------------------------
# 4. FINDING INFORMATION
# ---------------------------------------------------------
print("\n--- 4. FINDING INFORMATION ---")
grades = ["A", "B", "A", "C", "A", "B"]
print(f"Original grades: {grades}")

# count(item) -> Returns how many times a value appears in the list
a_count = grades.count("A")
print(f"1. count('A')          : {a_count} times")

# index(item) -> Returns the FIRST index position where the value is found
first_b_index = grades.index("B")
print(f"2. index('B')          : Found at index {first_b_index}")


# ---------------------------------------------------------
# 5. COPYING A LIST
# ---------------------------------------------------------
print("\n--- 5. COPYING A LIST ---")
print("CRITICAL: list2 = list1 does NOT copy. It links them together in memory!")

original = ["pizza", "burger"]

# copy() -> Creates a safe, independent clone of the list
safe_copy = original.copy()
safe_copy.append("fries")

print(f"Original list          : {original} (Unchanged)")
print(f"safe_copy list         : {safe_copy} (Changed)")

print("\n=====================================================")