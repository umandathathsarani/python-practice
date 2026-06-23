print("=====================================================")
print("             PYTHON 2D LISTS CHEAT SHEET             ")
print("=====================================================")

# ---------------------------------------------------------
# 1. Creating a 2D List
# ---------------------------------------------------------
print("\n--- 1. Creating a 2D List ---")
print("Think of it as a table with rows and columns.")

# A 3x3 matrix (3 rows, 3 columns)
matrix = [
    [1, 2, 3],  # Row 0
    [4, 5, 6],  # Row 1
    [7, 8, 9]   # Row 2
]

print("Our Matrix:")
for row in matrix:
    print(row)


# ---------------------------------------------------------
# 2. Accessing Elements [row][column]
# ---------------------------------------------------------
print("\n--- 2. Accessing Elements ---")
print("Syntax: list_name[row_index][column_index]")

print(f"Top-left element    (matrix[0][0]) : {matrix[0][0]}")
print(f"Middle element      (matrix[1][1]) : {matrix[1][1]}")
print(f"Bottom-right element(matrix[2][2]) : {matrix[2][2]}")


# ---------------------------------------------------------
# 3. Modifying Elements
# ---------------------------------------------------------
print("\n--- 3. Modifying Elements ---")
print("Changing the top-right number (3) to 99...")

matrix[0][2] = 99
print(f"New Row 0: {matrix[0]}")


# ---------------------------------------------------------
# 4. Iterating Through a 2D List
# ---------------------------------------------------------
print("\n--- 4. Iterating Through a 2D List ---")
print("Using nested loops to print every single item:")

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # Prints a newline after each row finishes


# ---------------------------------------------------------
# 5. Adding and Removing Rows/Items
# ---------------------------------------------------------
print("\n--- 5. Adding and Removing ---")

# Adding a completely new row
matrix.append([10, 11, 12])
print(f"After appending a new row: {matrix[-1]}")

# Adding a new item to a specific existing row (e.g., adding to Row 0)
matrix[0].append(100)
print(f"Row 0 after adding an extra item: {matrix[0]}")

# Removing a specific row
removed_row = matrix.pop(1)
print(f"Removed Row 1: {removed_row}")


# =========================================================
# 6. PRACTICAL EXAMPLE: Real-World Data Table
# =========================================================
print("\n=====================================================")
print("      PRACTICAL EXAMPLE: UNIVERSITY DATABASE         ")
print("=====================================================")

# Storing data as [Country, University Name, Status]
transfer_options = [
    ["Australia", "RMIT University", "Evaluating"],
    ["Canada", "University of Waterloo", "Shortlisted"],
    ["United Kingdom", "Manchester University", "Evaluating"],
    ["New Zealand", "Auckland University", "Pending"]
]

print("Current Transfer Evaluation Status:\n")

# Formatting the 2D list into a readable table
print(f"{'COUNTRY':<16} | {'UNIVERSITY':<25} | {'STATUS'}")
print("-" * 55)

for option in transfer_options:
    country = option[0]
    uni_name = option[1]
    status = option[2]
    
    # The :<16 formatting ensures the columns align perfectly!
    print(f"{country:<16} | {uni_name:<25} | {status}")

print("\n=====================================================")