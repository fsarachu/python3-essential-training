def b(n):
    print("{:08b}".format(n))  # Print binary representation of 'n'


x, y = 0x55, 0xaa

print("x: ", end='')
b(x)
print("y: ", end='')
b(y)

print("x | y: ", end='')
b(x | y)

print("x & y: ", end='')
b(x & y)

print("x ^ y: ", end='')
b(x ^ y)

print("x ^ x: ", end='')
b(x ^ x)

print("x << 2: ", end='')
b(x << 2)

print("x >> 5: ", end='')
b(x >> 5)
