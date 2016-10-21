a = 0
b = 1

if a < b:
    print('a ({}) is less than b ({})'.format(a, b))
else:
    print('b ({}) is less or equal than a ({})'.format(a, b))

print("foo" if a < b else "bar")  # Ternary operator-like conditional expression
