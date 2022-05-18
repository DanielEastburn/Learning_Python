# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1          # int
y = 2.5        # float
name = "John"  # str
is_cool = True # bool

# Multiple Assignment
z, c, lastName, male = (1, 2.5, "Dan", True)

print("Hello")
print(x, y, name, is_cool)
print(z, c, lastName, male)

# Basic Maths

a = x + y

print(a)
print(type(a), type(name), type(x), type(is_cool))

# Casting
x = str(x)
y = int(y)
z = float(y)

print(y, type(y))
print(z, type(z))