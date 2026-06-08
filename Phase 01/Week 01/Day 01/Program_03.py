# User Inputs

name = input("Enter your name here: ")
print("My name is : " + name + "\n")

print ('#' * 30)

print("\n")

yourName = input("What is your name? ")
favouriteColor = input("What is your favourite color? ")
print(yourName + " likes " + favouriteColor + ".")

print("-----------------------------------")

# Type Conversion

birth_year = input('Birth Year: ' )
print(type(birth_year))

age = 2026 - int(birth_year)
print(type(age))

print(age)


print("-----------------------------------")

weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
