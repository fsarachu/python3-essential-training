def isprime(n):
    if n <= 1:
        return False

    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        # Confusing for...else construct explained at:
        # http://python-notes.curiousefficiency.org/en/latest/python_concepts/break_else.html
        return True


for i in range(20):
    if isprime(i):
        print(i)
