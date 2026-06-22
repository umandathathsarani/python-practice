# Basic Syntax and Example


# 1. Initialize a control variable
count = 1

# 2. Define the loop condition
while count <= 5:
    print(f"Iteration number: {count}")
    
    # 3. Update the control variable to avoid an infinite loop
    count += 1 









# Control Statements: Break and Continue


# break: Immediately exits the loop entirely, ignoring the initial loop condition.

# continue: Skips the remaining code inside the current iteration and jumps straight to evaluating the loop's condition for the next round.


# Example using break and continue
number = 0
while number < 10:
    number += 1
    
    if number == 3:
        continue  # Skips printing 3 and jumps to the next iteration
        
    if number == 7:
        break   # Completely terminates the loop when reaching 7
        
    print(number)











# The while True Loop (Emulating Do-While)


# Python does NOT have a native do-while loop. However, you can emulate this behavior—where the code block always runs at least once—by pairing an intentional infinite while True loop with an internal if condition and a break statement. This is highly useful for validating user input.

while True:
    password = input("Enter the secret password: ")
    
    # The condition to break out of the loop
    if password == "python123":
        print("Access granted!")
        break
    else:
        print("Incorrect. Try again.")










# The while ... else Statement


# Python allows an optional else block at the end of a while loop. The code inside the else block runs only if the while loop completes normally by its condition naturally becoming False. If the loop is terminated prematurely by a break statement, the else block is completely skipped.

search_items = [1, 2, 3, 4, 5]
target = 10
index = 0

while index < len(search_items):
    if search_items[index] == target:
        print("Item found!")
        break
    index += 1
else:
    # This executes because index reached len(search_items) without a break
    print("Item not found in the list.")
