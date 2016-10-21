# Fibonacci series: the sum of two elements defines the next one
a, b = 0, 1

next_element = a + b

while next_element < 100:
    print(next_element)
    a = b
    b = next_element
    next_element = a + b

# For loops work with an iterator.
# That is an object that each time you call it it gives you the value of the next element
fh = open('lines.txt')

for line in fh.readlines():
    print(line)
