# For loops are used to iterate through an iterable
# All container types are iterables (lists, tuples, strings, etc.)

fh = open('lines.txt')

for line in fh.readlines():
    print(line, end='')

print("\n-------------")

for a in [1, 2, 3, 4, 5, 6]:
    print(a, end=' ')

print("\n-------------")

for a in 'string':
    print(a, end=' ')
