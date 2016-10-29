d = {'one': 1, 'two': 2, 'three': 3}

print('d : {}'.format(d))

d = dict(one=1, two=2, three=3)

print('d : {}'.format(d))

d2 = dict(**d, four=4, five=5, six=6)

print('d2 : {}'.format(d2))

print('\'one\' in d2 : {}'.format('one' in d2))

print('d2.get(\'three\') : {}'.format(d2.get('three')))
print('d2.get(\'ten\', \'Not found\') : {}'.format(d2.get('ten', 'Not found')))
