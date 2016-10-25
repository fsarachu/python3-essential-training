fh = open('lines.txt')

# Get line index
for index, line in enumerate(fh.readlines()):
    print(index, line, end='')

print('\n------------------')

# Get index number of s occurences
s = 'This is a string'

for i, c in enumerate(s):
    if c == 's':
        print("Index {} is an s".format(i))
