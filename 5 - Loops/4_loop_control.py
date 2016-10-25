s = 'this is a string'

for c in s:
    print(c, end=' ')

print("\n--------------------")

for c in s:
    if c == 's':
        continue
    print(c, end=' ')

print("\n--------------------")

