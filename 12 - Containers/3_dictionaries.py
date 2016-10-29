d = {'one': 1, 'two': 2, 'three': 3}

print('d : {}'.format(d))

d = dict(one=1, two=2, three=3)

print('d : {}'.format(d))

d2 = dict(**d, four=4, five=5, six=6)
