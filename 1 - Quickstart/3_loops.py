# Fibonacci series: the sum of two elements defines the next one
a, b = 0, 1

next_element = a + b

while next_element < 100:
    print(next_element)
    a = b
    b = next_element
    next_element = a + b
