# Basic if Statement
score = 85

if score >= 50:
    print("You passed!")  # Runs only because score is greater than 50





# Adding an else Clause
age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You are too young to vote.")  # Runs because age is less than 18





# Checking Multiple Conditions with elif
temperature = 25

if temperature > 30:
    print("It is hot outside.")
elif temperature > 18:
    print("The weather is pleasant.")  # Runs because 25 is > 18
else:
    print("It is cold outside.")





# Combining Conditions with Logical Operators

# and: Returns True if both statements are true.
# or: Returns True if at least one statement is true.
# not: Reverses the boolean result of the condition

has_ticket = True
is_registered = False

# Requires both to be True
if has_ticket and is_registered:
    print("Welcome to the event!")
else:
    print("Access denied.")  # Runs because is_registered is False





# One-Line Shorthand (Ternary Operator)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Outputs: Adult