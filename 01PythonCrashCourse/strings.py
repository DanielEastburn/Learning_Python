# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Daniel"
age = 25

print("Hello, my name is " + name + " and I am " + str(age))

# String Formatting

#Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

#F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')

# String Methods

string = "String Methods"

# Capitalize string
print(string.capitalize())

# Make all uppercase
print(string.upper())

# Make all lowercase
print(string.lower())

# Swap Case
print(string.swapcase())

# Get length
print(len(string))

# Replace
print(string.replace("Methods", "Pethods"))

# Count
sub = "h"
print(string.count(sub))

# Starts with
print(string.startswith('String'))

# Ends with 
print(string.endswith('s'))

# Split into a List
print(string.split())

# Find position 
print(string.find('i'))

# Is all alphanumeric
print(string.isalnum())

# Is all alphabetic
print(string.isalpha())

# Is all numeric
print(string.isnumeric())