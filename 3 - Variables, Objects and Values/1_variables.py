# In Python 3 EVERYTHING is an object
# Every object has an id, a class type and a value

a = 4
print("id: {}".format(id(a)))  # Object id
print("type: {}".format(type(a)))
print("value: {}".format(a))

print("---------------------------")

a = "Hello"
print("id: {}".format(id(a)))  # Now 'a' refers to another object
print("type: {}".format(type(a)))
print("value: {}".format(a))

print("---------------------------")

a = 4
print("id: {}".format(id(a)))  # Same id as in the first assignment! :O
print("type: {}".format(type(a)))
print("value: {}".format(a))
