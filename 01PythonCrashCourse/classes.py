# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create Class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}.'

    def has_birthday(self):
        self.age += 1


# Extend class

class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balace is {self.balance}.'

# Init user object
dan = User('Daniel Eastburn', 'dan@gmail.com', 25)

# Init customer object
alex = Customer('Alex Hayes', 'alex@yahoo.com', 23)

alex.set_balance(500)
print(alex.greeting())


print(dan.name, type(dan))

dan.has_birthday()
print(dan.greeting())