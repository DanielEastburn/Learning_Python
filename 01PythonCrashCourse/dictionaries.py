# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create Dictionary class: dict
person = {
    'first_name': 'Daniel',
    'last_name': 'Eastburn',
    'age': 25
}

print(person, type(person))

# Use constructor

person2 = dict(first_name='Abigail', last_name='Kinslow')
print(person2)

# Get Value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person3 = person.copy()
person3['city'] =  'Warrington'
print(person3)

# Remove item
del(person['age'])
person.pop('phone')
print(person)

# Clear
person.clear
print(person)

# Get lenth
print(len(person3))

# List of dict
people = [
    {'name': 'Alex', 'age': 23},
    {'name': 'Iain', 'age': 24}
]

print(people[0]['name'])




