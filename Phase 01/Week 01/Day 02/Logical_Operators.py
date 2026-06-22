print("=====================================================")
print("         PYTHON LOGICAL OPERATORS CHEAT SHEET        ")
print("=====================================================")

# Defining variables to use in our examples
a = True
b = False

x = 5
y = 10

print(f"Variables used for examples:")
print(f" a = {a}, b = {b}")
print(f" x = {x}, y = {y}\n")

# ---------------------------------------------------------
# 1. AND Operator (and)
# Returns True if BOTH statements/conditions are true
# ---------------------------------------------------------
print("--- 1. AND Operator (and) ---")
print(f"a and b                  ->  {a and b}")
print(f"True and True            ->  {True and True}")

# Combining with comparison operators:
# (5 < 10) is True AND (10 > 5) is True  => True
print(f"(x < 10) and (y > 5)     ->  {(x < 10) and (y > 5)}")  

# (5 < 10) is True AND (10 < 5) is False => False
print(f"(x < 10) and (y < 5)     ->  {(x < 10) and (y < 5)}\n") 


# ---------------------------------------------------------
# 2. OR Operator (or)
# Returns True if at least ONE of the statements is true
# ---------------------------------------------------------
print("--- 2. OR Operator (or) ---")
print(f"a or b                   ->  {a or b}")
print(f"False or False           ->  {False or False}")

# Combining with comparison operators:
# (5 < 10) is True OR (10 < 5) is False => True (because at least one is True)
print(f"(x < 10) or (y < 5)      ->  {(x < 10) or (y < 5)}")   

# (5 > 10) is False OR (10 < 5) is False => False (because neither is True)
print(f"(x > 10) or (y < 5)      ->  {(x > 10) or (y < 5)}\n")  


# ---------------------------------------------------------
# 3. NOT Operator (not)
# Reverses the result (True becomes False, False becomes True)
# ---------------------------------------------------------
print("--- 3. NOT Operator (not) ---")
print(f"not a                    ->  {not a}")
print(f"not b                    ->  {not b}")

# Reversing a comparison:
# (x < 10 and y > 5) is True, so not(True) => False
print(f"not(x < 10 and y > 5)    ->  {not((x < 10) and (y > 5))}\n")

print("=====================================================")