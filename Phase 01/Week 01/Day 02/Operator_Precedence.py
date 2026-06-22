# Operator Precedence (PEMDAS)


# When evaluating long math expressions, Python follows standard algebraic rules of precedence:

# 1. Parentheses () (highest priority)

# 2. Exponentiation **

# 3. Multiplication *, Division /, Floor Division //, Modulus % (evaluated left-to-right)

# 4. Addition +, Subtraction - (evaluated left-to-right)



# Example of operator precedence
result = 5 + 3 * 2 ** 2  # 2**2 = 4 -> 4*3 = 12 -> 12+5 = 17
print(result) # Output: 17

# Overriding precedence with parentheses
result_two = (5 + 3) * 2
print(result_two) # Output: 16
