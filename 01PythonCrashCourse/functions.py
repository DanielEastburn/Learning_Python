# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name):
    print(f'Hello {name}')

sayHello('Daniel Eastburn')

# Define parameter in funtion
def sayHello2(name='Alex'):
    print(f'Hello {name}')

sayHello2()

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(3, 4))

num = getSum(2, 7)
print(num)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSumlam = lambda num1, num2 : num1 + num2

print(getSumlam(10, 4))

