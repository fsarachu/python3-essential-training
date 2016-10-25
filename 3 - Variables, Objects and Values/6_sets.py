# A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries.

# Empty set
s = set()  # Note that "s = {}" would create an empty dictionary
print("s: {}".format(s))

# Duplicates are automatically removed
animals = {'kangaroo', 'elephant', 'jaguar', 'elephant', 'lion'}
print(animals)

# Membership testing
print("'kangaroo' in animals: {}".format('kangaroo' in animals))
print("'dog' in animals: {}".format('dog' in animals))

# Set operations
a = set('abracadabra')
b = set('alacazam')

print("a: {}".format(a))  # unique letters in a
print("a - b: {}".format(a - b))  # letters in a but not in b
print("a | b: {}".format(a | b))  # letters in either a or b
print("a & b: {}".format(a & b))  # letters in both a and b
print("a ^ b: {}".format(a ^ b))  # letters in a or b but not both
