print("=====================================================")
print("           PYTHON NESTED LOOPS CHEAT SHEET           ")
print("=====================================================")

# ---------------------------------------------------------
# 1. The Basic Concept (How execution flows)
# ---------------------------------------------------------
print("\n--- 1. Basic Nested For Loop (Coordinates) ---")
for x in range(1, 4):         # Outer loop
    for y in range(1, 3):     # Inner loop
        print(f"Outer x={x}, Inner y={y}")


# ---------------------------------------------------------
# 2. Iterating Through a 2D List (Matrix)
# ---------------------------------------------------------
print("\n--- 2. Iterating Through a 2D List ---")
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in number_grid:
    for item in row:
        print(item, end=" ")
print("\n")


# ---------------------------------------------------------
# 3. Simple Example: Outfit Combinations
# ---------------------------------------------------------
print("\n--- 3. Simple Example: Outfit Combinations ---")
print("Pairing every shirt with every pair of pants:")

shirts = ["Red Shirt", "Blue Shirt"]
pants = ["Jeans", "Chinos"]

for shirt in shirts:
    for pant in pants:
        print(f"Outfit: {shirt} + {pant}")


# ---------------------------------------------------------
# 4. Simple Example: A Digital Clock
# ---------------------------------------------------------
print("\n--- 4. Simple Example: A Digital Clock ---")
print("Simulating 2 hours, and the first 3 minutes of each hour:")

for hour in range(1, 3):           # Hours 1 and 2
    for minute in range(1, 4):     # Minutes 1, 2, and 3
        print(f"Time -> {hour}:0{minute}")


# ---------------------------------------------------------
# 5. Using 'break' in a Nested Loop
# ---------------------------------------------------------
print("\n--- 5. Using 'break' inside Nested Loops ---")
for a in range(1, 4):           
    print(f"Start Outer: {a}")
    for b in range(1, 4):
        if b == 2:
            print("   Inner loop breaks at b=2!")
            break               # ONLY stops the 'b' loop!
        print(f"   Inner: {b}")


# =========================================================
# 6. THE BIG COMPLEX CODE: All Loops Combined
# =========================================================
print("\n=====================================================")
print("      THE ULTIMATE LOOP CHALLENGE: CAMPUS SYSTEM     ")
print("=====================================================")
print("Scenario: Processing Software Engineering students at ")
print("the Malabe campus for university-organized sports.")
print("This combines while, for, nested loops, break, and continue!\n")

it_students = ["Amal", "Kamal"]
sports_activities = ["Badminton", "Track", "Volleyball"]

# 1. OUTermost loop (A while loop tracking days)
day = 1
while day <= 2:
    print(f"\n>>> [OPEN] Registration Day {day} at Malabe Campus <<<")

    # 2. INNER loop 1 (Iterating over our list of students)
    for student in it_students:
        print(f"\n  Evaluating {student}'s sports applications...")

        # 3. INNER loop 2 (Nested for loop checking sports)
        for sport in sports_activities:
            
            # Using CONTINUE to skip a specific condition entirely
            if sport == "Track":
                print(f"    -> {sport}: Track is closed for maintenance! Skipping.")
                continue  
            
            print(f"    -> {sport}: Processing...")

            # 4. INNER loop 3 (Nested while loop for a 2-step approval)
            step = 1
            while step <= 2:
                # Using BREAK to stop a specific condition early
                if step == 2 and sport == "Volleyball":
                    print("      [!] Missing medical form. Halting Volleyball approval.")
                    break  # This breaks the "step" while loop, NOT the "sport" for loop
                
                print(f"      Step {step} cleared.")
                step += 1

        # The 'else' clause on a for loop (Executes if the loop finishes without hitting a break)
        else:
            print(f"  *** All available sports checked for {student} without system errors. ***")

    print(f"\n>>> [CLOSE] End of Day {day} <<<")
    day += 1

print("\n=====================================================")