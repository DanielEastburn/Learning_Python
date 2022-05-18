# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
vehicles = ('Cars', 'Vans', 'Bikes')
# Create tuple with constructor
vehicles2 = tuple(('Cars', 'Vans', 'Bikes'))

print(vehicles, type(vehicles))

# Single value needs trailing comma
vehicles3 = ('Cars',)

# Get value
print(vehicles[1])

# Can't change value
# vehicles[0] = 'Trucks'

# Delete tuple
del vehicles2
#print(vehicles2)

#len    
print(len(vehicles))


# A Set is a collection which is unordered and unindexed. No duplicate members.

vehicles_set = {'Cars', 'Trains', 'Planes'}

# Check if in set
print('Cars' in vehicles_set)

# Add to set
vehicles_set.add('Trucks')
print(vehicles_set)

# Can't add duplicates - no error, just appears once
vehicles_set.add('Trucks')
print(vehicles_set)

# Remove from set
vehicles_set.remove('Cars')
print(vehicles_set)

# Clear set
vehicles_set.clear()

# Delete
del vehicles_set
