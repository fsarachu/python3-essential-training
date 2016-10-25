# Tuples are immutable, and usually contain a heterogeneous sequence of elements
# that are accessed via unpacking or indexing

t = 12345, 54321, 'hello!'

print("t: {}".format(t))
print("t[0]: {}".format(t[0]))

# Empty tuple:
empty = ()
print("empty: {}".format(empty))
print("len(empty): {}".format(len(empty)))

# Tuple of only 1 element:
singleton = 'hello',
print("singleton: {}".format(singleton))
print("len(singleton): {}".format(len(singleton)))
