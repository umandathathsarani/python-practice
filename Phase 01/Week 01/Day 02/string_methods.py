course = "Python for Beginners"
#         0123456789.........19

print(len(course)) # 20
# len and print are general purpose functions. They don't belong to strings or numbers or any kind of objects.

print(course)

# String Methods
print(course.upper())

print(course.lower())

print(course.title())

print(course.find('P') ) # 0 

print(course.find('o') ) # 4 -- find method is case sensitive

print(course.find('O') ) # -1

print(course.find('Beginners') ) # 11

print(course.replace('Beginners', 'Absolute Beginners')) # Python for Absolute Beginners

# replace -- Case sensitive 
print(course.replace('beginners', 'Absolute Beginners')) # Python for Beginners

print('Python' in course) # True -- Case sensitive

print('python' in course) # False


# find() --> Returns the index of the character or sequence of characters

# in --> Produces a boolean value