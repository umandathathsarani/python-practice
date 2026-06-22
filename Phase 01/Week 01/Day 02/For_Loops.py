print("=====================================================")
print("         THE ULTIMATE PYTHON FOR LOOPS CHEAT SHEET   ")
print("=====================================================")

# ---------------------------------------------------------
# 1. Looping Through a Range of Numbers (Basic & Advanced)
# ---------------------------------------------------------
print("\n--- 1. Using range() ---")
print("Basic range(5) -> 0 to 4:")
for i in range(5):
    print(i, end=" ")  # 'end=" "' prints on the same line

print("\n\nRange with start and stop (2 to 6):")
for i in range(2, 7):
    print(i, end=" ")

print("\n\nRange with steps (Count by 2s from 0 to 8):")
for i in range(0, 10, 2):
    print(i, end=" ")

print("\n\nCounting backwards (5 down to 1):")
for i in range(5, 0, -1):
    print(i, end=" ")
print("\n")


# ---------------------------------------------------------
# 2. Iterating Over Collections (Lists, Strings, Tuples, Sets)
# ---------------------------------------------------------
print("\n--- 2. Iterating Over Collections ---")

print("Looping through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\nLooping through a string:")
for letter in "AI":
    print(letter)


# ---------------------------------------------------------
# 3. Getting Both Index and Value (enumerate)
# ---------------------------------------------------------
print("\n--- 3. Getting Both Index and Value ---")
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"Index {index}: {name}")


# ---------------------------------------------------------
# 4. Iterating Over Dictionaries
# ---------------------------------------------------------
print("\n--- 4. Iterating Over Dictionaries ---")
user = {"name": "Sam", "role": "Admin"}

print("Looping through keys and values together:")
for key, value in user.items():
    print(f"{key}: {value}")

print("\nLooping just through values:")
for value in user.values():
    print(value)


# ---------------------------------------------------------
# 5. Loop Control Statements (break & continue)
# ---------------------------------------------------------
print("\n--- 5. Loop Control Statements ---")
for num in range(1, 6):
    if num == 3:
        print("Skipping 3!")
        continue  # Skips 3 and jumps to the next iteration
    
    if num == 5:
        print("Breaking at 5!")
        break     # Stops the loop entirely when it hits 5
        
    print(f"Number: {num}")


# ---------------------------------------------------------
# 6. The 'else' Clause in Loops
# ---------------------------------------------------------
print("\n--- 6. The 'else' Clause in a Loop ---")
print("The else block runs ONLY if the loop finishes normally (no break).")

for i in range(3):
    print(f"Normal loop iteration {i}")
else:
    print("Loop finished successfully without breaking!")


# ---------------------------------------------------------
# 7. Nested Loops (A Loop inside a Loop)
# ---------------------------------------------------------
print("\n--- 7. Nested Loops ---")
print("Creating coordinates (x, y):")

for x in range(1, 3):       # Outer loop
    for y in range(1, 4):   # Inner loop
        print(f"({x}, {y})")


# ---------------------------------------------------------
# 8. Iterating Multiple Lists at Once (zip)
# ---------------------------------------------------------
print("\n--- 8. Iterating Multiple Lists (zip) ---")
print("Combining names and scores:")

students = ["John", "Emma", "Kelly"]
scores = [85, 92, 78]

# zip() pairs the first items together, second items together, etc.
for student, score in zip(students, scores):
    print(f"{student} scored {score}")


# ---------------------------------------------------------
# 9. List Comprehensions (Pro-Tip: One Line Loops)
# ---------------------------------------------------------
print("\n--- 9. List Comprehensions (One-Line Loops) ---")
print("Creating a list of squares using a standard loop:")
squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)

print("\nDoing the exact same thing in one line:")
fast_squares = [i * i for i in range(1, 6)]
print(fast_squares)

print("\n=====================================================")