# Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”.
# Dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.
# It is best to think of a dictionary as an unordered set of key: value pairs, keys are unique (within one dictionary).
# The main operations on a dictionary are storing a value with some key and extracting the value given the key.

# Create a simple dictionary
tel = {'Max': 421324, 'John': 432857}  # Or: tel = dict(Max=421324, John=432857)
print("tel: {}".format(tel))

# Add new pair
tel['Eric'] = 439943
tel['Brian'] = 436709
print("tel: {}".format(tel))

# Delete a pair
del tel['Max']
print("tel: {}".format(tel))

# Retrieve all keys
print("list(tel.keys()): {}".format(list(tel.keys())))

# Retrieve all keys sorted
print("sorted(tel.keys()): {}".format(sorted(tel.keys())))

# Check if a key is in the dictionary
print("'Brian' in tel: {}".format('Brian' in tel))
print("'Jack' in tel: {}".format('Jack' in tel))
print("'Jack' not in tel: {}".format('Jack' not in tel))

# Dictionary comprehension
power = {x: x ** 2 for x in (1, 2, 3, 4, 5, 6)}
print("power: {}".format(power))
