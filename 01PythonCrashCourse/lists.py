# A List is a collection which is ordered and changeable. Allows duplicate members.

# Lists are Like Arrays

# Create List
numbers = [1, 2, 3, 4, 5]

# Use and constructor
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)


meats = ['Steak', 'Lamb', 'Chicken', 'Duck']

# Get a Value
print(meats[1])

# Get length
print(len(meats))

# Append to list
meats.append('Liver')
print(meats)

# Remove from list
meats.remove('Lamb')
print(meats)

# Insert into position
meats.insert(2, 'Pork')
print(meats)

# Change Value
meats[0] = 'Beef'
print(meats)

# Remove with pop
meats.pop(2)
print(meats)

# Reverse list
meats.reverse()
print(meats)

# Sort List
meats.sort()
print(meats)

# Reverse sort
meats.sort(reverse=True)
print(meats)
