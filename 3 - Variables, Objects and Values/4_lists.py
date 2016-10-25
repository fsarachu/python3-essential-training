# A list is mutable, but less efficient than a tuple
x = [1, 2, 3]
x.append(5)
x.insert(3, 4)
print(type(x), x)
