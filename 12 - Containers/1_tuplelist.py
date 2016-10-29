# Tuple is inmutable, lighter and faster than lists
t = 1, 2, 3, 4, 5

print('t: {}'.format(t))

print('t[0]: {}'.format(t[0]))
print('t[4]: {}'.format(t[4]))
print('t[-2]: {}'.format(t[-2]))

print('len(t): {}'.format(len(t)))
print('min(t): {}'.format(min(t)))
print('max(t): {}'.format(max(t)))

print("------------------------")

# List is mutable, slower and heavier than tuples but more powerful
l = [1, 2, 3, 4, 5]

print('l: {}'.format(l))

print('ll[0]: {}'.format(l[0]))
print('l[4]: {}'.format(l[4]))
print('l[-2]: {}'.format(l[-2]))

print('len(l): {}'.format(len(l)))
print('min(l): {}'.format(min(l)))
print('max(l): {}'.format(max(l)))
