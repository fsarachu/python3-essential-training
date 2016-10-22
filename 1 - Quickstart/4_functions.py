def isprime(n):
    if n == 1:
        print("  1 is special.")
        return False

    for x in range(2, n):
        if n % x == 0:
            print("  {} is divisible by {}".format(n, x))
            return False
    else:
        # Confusing for...else construct explained at:
        # http://python-notes.curiousefficiency.org/en/latest/python_concepts/break_else.html
        print("* {} is a prime number".format(n))
        return True


for i in range(20):
    isprime(i)
