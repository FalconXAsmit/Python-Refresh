# Variable are containers for storing data values.
# In Python, variables do not need to be declared with any particular type and can even change type after they have been set.
# Variable names can be any length and can consist of letters, numbers, and underscores.

age = 18  # Integer
name = "Asmit"  # String
height = 180.34  # Float
is_student = True  # Boolean

# Printing the variables and their types
print("Age:", age, " ", type(age))
print("Name:", name,  " ", type(name))
print("Height:", height, " ", type(height))
print("Is Student:", is_student, " ", type(is_student))

# Multiple variable assignment
x, y, z = 5, 10.5, "Hello" # in python, you can assign multiple variables in one line

# To input a variable from the user
color = input("Enter your favorite color: ") # This will take input from the user, this always returns a string to convert it to other types you can use int(), float() etc.
print("Favorite Color:", color, " ", type(color))

# Example of type conversion
score = float(input("Enter your exam score: "))  # Converts the input string to an integer
print("Entered Score:", score, " ", type(score))