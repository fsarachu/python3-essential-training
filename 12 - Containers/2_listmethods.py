x = list(range(20))

print('x: {}'.format(x))
print('10 in x : {}'.format(10 in x))
print('50 in x : {}'.format(50 in x))
print('50 not in x : {}'.format(50 not in x))
print('x.count(5) : {}'.format(x.count(5)))
print('x.index(5) : {}'.format(x.index(5)))
print('len(x) : {}'.format(len(x)))

x.extend(range(20, 40))

print('x.extend(range(20, 40)) : {}'.format(x))
