import math

print("=====================================================")
print("         PYTHON MATH FUNCTIONS CHEAT SHEET           ")
print("=====================================================")

# ---------------------------------------------------------
# Built-in Math Functions (No Import Needed)
# ---------------------------------------------------------
print("\n--- Built-in Math Functions (No Import Needed) ---")
print("These elementary functions are global and available everywhere in Python:")

print(f"abs(-15)              = {abs(-15)} \t\t# Returns absolute value.")
print(f"round(3.14159, 2)     = {round(3.14159, 2)} \t\t# Rounds to n digits.")
print(f"max(5, 12, 8, 3)      = {max(5, 12, 8, 3)} \t\t# Returns largest value.")
print(f"min(5, 12, 8, 3)      = {min(5, 12, 8, 3)} \t\t# Returns smallest value.")
print(f"pow(2, 4)             = {pow(2, 4)} \t\t# Raises x to power y.")
print(f"sum([10, 20, 30])     = {sum([10, 20, 30])} \t\t# Sums up items.")


print("\n=====================================================")
print("              The `math` Module Functions            ")
print("=====================================================")

# ---------------------------------------------------------
# 1. Number Representation & Rounding
# ---------------------------------------------------------
print("\n--- 1. Number Representation & Rounding ---")
print(f"math.ceil(4.2)        = {math.ceil(4.2)} \t\t# Rounds up to nearest integer.")
print(f"math.floor(4.8)       = {math.floor(4.8)} \t\t# Rounds down to nearest integer.")
print(f"math.fabs(-5.5)       = {math.fabs(-5.5)} \t\t# Returns float absolute value.")
print(f"math.factorial(5)     = {math.factorial(5)} \t\t# Returns factorial of integer.")
print(f"math.gcd(12, 18)      = {math.gcd(12, 18)} \t\t# Greatest common divisor.")

# ---------------------------------------------------------
# 2. Powers, Roots, & Logarithms
# ---------------------------------------------------------
print("\n--- 2. Powers, Roots, & Logarithms ---")
print(f"math.sqrt(16)         = {math.sqrt(16)} \t# Returns square root.")
print(f"math.cbrt(27)         = {math.cbrt(27)} \t# Returns cube root.")
print(f"math.log(10)          = {math.log(10):.4f} \t# Natural log, or log of custom base.")
print(f"math.log(16, 2)       = {math.log(16, 2)} \t# Log of custom base (16 base 2).")
print(f"math.log10(100)       = {math.log10(100)} \t# Base-10 logarithm.")
print(f"math.exp(2)           = {math.exp(2):.4f} \t# Returns e^x.")

# ---------------------------------------------------------
# 3. Trigonometry & Angular Conversion
# ---------------------------------------------------------
print("\n--- 3. Trigonometry & Angular Conversion ---")
print("Note: Trigonometric inputs and outputs always assume radians, not degrees.")
print(f"math.sin(math.pi/2)   = {math.sin(math.pi/2)} \t# Sine of angle.")
print(f"math.cos(math.pi)     = {math.cos(math.pi)} \t# Cosine of angle.")
print(f"math.tan(math.pi/4)   = {math.tan(math.pi/4):.4f} \t# Tangent of angle.")
print(f"math.radians(180)     = {math.radians(180):.4f} \t# Converts degrees to radians.")
print(f"math.degrees(math.pi) = {math.degrees(math.pi)} \t# Converts radians to degrees.")
print(f"math.hypot(3, 4)      = {math.hypot(3, 4)} \t# Returns Euclidean norm/hypotenuse.")

# ---------------------------------------------------------
# 4. Built-in Mathematical Constants
# ---------------------------------------------------------
print("\n--- 4. Built-in Mathematical Constants ---")
print(f"math.pi               = {math.pi:.5f} \t# π ≈ 3.14159")
print(f"math.e                = {math.e:.5f} \t# e ≈ 2.71828")
print(f"math.tau              = {math.tau:.5f} \t# τ ≈ 6.28318")
print(f"math.inf              = {math.inf} \t\t# Floating-point positive infinity")
print(f"math.nan              = {math.nan} \t\t# Floating-point 'Not a Number' value")
print("\n=====================================================")