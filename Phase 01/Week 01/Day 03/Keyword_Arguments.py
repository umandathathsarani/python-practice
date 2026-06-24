print("=====================================================")
print("        PYTHON KEYWORD ARGUMENTS CHEAT SHEET         ")
print("=====================================================")

# Let's set up a base function to use for our examples
def register_student(name, major, campus):
    print(f"Registered {name} for {major} at the {campus} campus.")


# ---------------------------------------------------------
# 1. The Standard Way (Positional) vs. Keyword
# ---------------------------------------------------------
print("\n--- 1. Positional vs. Keyword ---")

# Standard Positional: You MUST remember the exact order
print("Positional : ", end="")
register_student("Amal", "Software Engineering", "Malabe")

# Keyword Arguments: You name the parameters, so order DOES NOT matter
print("Keyword    : ", end="")
register_student(campus="Malabe", name="Amal", major="Software Engineering")


# ---------------------------------------------------------
# 2. Why use Keyword Arguments? (Readability)
# ---------------------------------------------------------
print("\n--- 2. The Power of Readability ---")
print("Keyword arguments make it obvious what data means.")

def set_permissions(read, write, execute):
    print(f"Permissions set -> Read: {read}, Write: {write}, Execute: {execute}")

# Bad Readability (What do these Trues and Falses mean?):
# set_permissions(True, False, True)

# Excellent Readability (Using keywords):
set_permissions(read=True, write=False, execute=True)


# ---------------------------------------------------------
# 3. Mixing Positional and Keyword Arguments
# ---------------------------------------------------------
print("\n--- 3. Mixing Argument Types ---")
print("CRITICAL RULE: Positional arguments MUST come before keyword arguments.")

# VALID: 'name' is positional (1st), the rest are keyword arguments
print("Valid Mix  : ", end="")
register_student("Zoe", campus="Kandy", major="Data Science")

# INVALID: This will crash your program with a SyntaxError!
# register_student(name="Zoe", "Data Science", "Kandy") 
# -> SyntaxError: positional argument follows keyword argument


# ---------------------------------------------------------
# 4. Keyword-Only Arguments (Advanced)
# ---------------------------------------------------------
print("\n--- 4. Enforcing Keyword-Only Arguments ---")
print("If you put an asterisk (*) in your parameters, everything after it MUST be a keyword argument.")

def create_server(ip_address, *, port, secure):
    print(f"Server at {ip_address}:{port} (Secure: {secure})")

# Valid: ip_address is positional, port and secure MUST be keywords
create_server("192.168.1.1", port=8080, secure=True)

# Invalid: This would crash because we didn't use keywords for port and secure
# create_server("192.168.1.1", 8080, True) 
# -> TypeError: create_server() takes 1 positional argument but 3 were given


print("\n=====================================================")