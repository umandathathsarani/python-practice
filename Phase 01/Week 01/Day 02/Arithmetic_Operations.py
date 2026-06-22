#                         + Addition (x + y)
# Adds two values

print(10 + 3) # 13



#                       - Subtraction (x - y)
# Subtracts right operand from left operand

print(10 - 3) # 7



#                     * Multiplication (x * y)
# Multiplies two values

print(10 * 3) # 30



#                     / Float Division (x / y)
# Divides and always returns a float

print(10 / 3) # 3.3333333333333335



#                     // Floor Division (x // y)
# Divides and rounds down to nearest whole number

print(10 // 3) # 3



#                          % Modulus (x % y)
# Divides and returns the remainder

print(10 % 3) # 1



#                     ** Exponentiation (x ** y)
# Raises left operand to the power of right operand10 ** 31000

print(10 ** 3) # 1000




#                     Important Behaviors to Keep in Mind


# 1. Float Division vs. Floor Division

# Float Division (/) always outputs a float, even if the numbers divide perfectly. 
# For example, 4 / 2 results in 2.0.

# Floor Division (//) cuts off everything after the decimal point and yields an integer. 
# However, if at least one input is a float, the result will still be returned as a float (e.g., 10.0 // 3 results in 3.0). 
# For negative numbers, floor division rounds down away from zero (e.g., -10 // 3 results in -4).


# 2. Shorthand Assignment Operators

# Python offers augmented assignment operators to modify a variable's value in place more cleanly:

x = 4

# x += 5 is equivalent to x = x + 5
x += 5
print(x)

x = 4

x = x + 5
print(x)


x = 4

# x -= 2 is equivalent to x = x - 2
x -= 2
print(x)

x = 4

x = x - 2
print(x)


x = 4

# x *= 3 is equivalent to x = x * 3
x *= 3
print(x)

x = 4

x = x * 3
print(x)


x = 4

# x /= 4 is equivalent to x = x / 4
x /= 4
print(x)

x = 4

x = x / 4
print(x)








                              # Code Blueprint
# Initialize variables
num1 = 15
num2 = 4

# Execute calculations
add_res = num1 + num2
sub_res = num1 - num2
mul_res = num1 * num2
div_res = num1 / num2
floor_res = num1 // num2
mod_res = num1 % num2
exp_res = num1 ** num2

# Display results
print(f"Addition:       {num1} + {num2}  = {add_res}")
print(f"Subtraction:    {num1} - {num2}  = {sub_res}")
print(f"Multiplication: {num1} * {num2}  = {mul_res}")
print(f"Float Division: {num1} / {num2}  = {div_res}")
print(f"Floor Division: {num1} // {num2} = {floor_res}")
print(f"Modulus:        {num1} % {num2}  = {mod_res}")
print(f"Exponent:       {num1} ** {num2} = {exp_res}")
