s = 'this is a string'

print("\n--- Normal for loop ---")

for c in s:
    print(c, end=' ')

print("\n\n--- Continue if a 's' is found ---")

for c in s:
    if c == 's':
        continue
    print(c, end=' ')

print("\n\n--- Break if a 's' is found ---")

for c in s:
    if c == 's':
        break
    print(c, end=' ')

print("\n\n--- Break if a 's' is found and print message if the loop has completed ---")

for c in s:
    if c == 's':
        break
    print(c, end=' ')
else:
    print('\nLoop completed successfully')

print("\n\n--- Break if a 'w' is found and print message if the loop has completed ---")

for c in s:
    if c == 'w':
        break
    print(c, end=' ')
else:
    print('\nLoop completed successfully')

