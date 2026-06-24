print("=====================================================")
print("      PYTHON REUSABLE FUNCTIONS CHEAT SHEET          ")
print("=====================================================")

# ---------------------------------------------------------
# 1. The Anti-Pattern (What NOT to do)
# ---------------------------------------------------------
print("\n--- 1. A Non-Reusable Function ---")
print("This function is bad because it hardcodes data and forces a print statement.")

def bad_greeting():
    name = "Amal"  # Hardcoded! We can only ever greet Amal.
    print(f"Hello, {name}!") # Forces a print! What if we want to save the greeting to a file?

bad_greeting()


# ---------------------------------------------------------
# 2. The Fix: Parameters and Returns
# ---------------------------------------------------------
print("\n--- 2. A Highly Reusable Function ---")
print("Good functions take IN data (parameters) and give OUT data (return).")

def generate_greeting(name, time_of_day="day"):
    # It does exactly one job: formatting a string.
    return f"Good {time_of_day}, {name.capitalize()}!"

# Now we can reuse this function in a dozen different ways:
print(generate_greeting("Zoe", "morning"))

# We can save it to a database, send it in an email, or just print it!
message = generate_greeting("sam", "evening")
print(f"Saved message ready to send: '{message}'")


# ---------------------------------------------------------
# 3. The Single Responsibility Principle
# ---------------------------------------------------------
print("\n--- 3. Single Responsibility ---")
print("A reusable function should only do ONE thing.")

# BAD: Calculates the price AND prints the receipt
def process_order(price, tax):
    total = price + (price * tax)
    print(f"Your total is ${total}")

# GOOD: Split it into two reusable parts!
def calculate_total(price, tax):
    return price + (price * tax)

def print_receipt(total_amount):
    print(f"--- RECEIPT ---\nTotal Due: ${total_amount:.2f}\n---------------")

# Now I can calculate a total WITHOUT printing a receipt if I want to!
cart_total = calculate_total(100, 0.08)
print_receipt(cart_total)


# ---------------------------------------------------------
# 4. Adding Docstrings (Documentation)
# ---------------------------------------------------------
print("\n--- 4. Docstrings (Making it readable for others) ---")
print("Professional functions use triple quotes (''' or \"\"\") to explain how they work.")

def celsius_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    
    Parameters:
    celsius (int/float): The temperature in degrees Celsius.
    
    Returns:
    float: The converted temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

print(f"25C is {celsius_to_fahrenheit(25)}F")

# Python has a built-in help() function that reads your Docstrings!
print("\n(Check the code to see how Docstrings work behind the scenes!)")
# Uncomment the line below to see what help() does in your terminal:
# help(celsius_to_fahrenheit) 


# ---------------------------------------------------------
# 5. Real-World Utility Example
# ---------------------------------------------------------
print("\n--- 5. Real-World Utility Example ---")
print("A classic reusable function: cleaning up messy user input.")

def clean_username(raw_input):
    """Strips whitespace, makes it lowercase, and removes bad characters."""
    clean = raw_input.strip()       # Remove leading/trailing spaces
    clean = clean.lower()           # Convert to lowercase
    clean = clean.replace("@", "")  # Remove accidental @ symbols
    return clean

messy_data = ["  Amal123  ", "@Zoe_Dev", "  Sam!  "]

for messy in messy_data:
    print(f"Cleaned username: '{clean_username(messy)}'")

print("\n=====================================================")