# There are two types of conditionals in python:
#   - Conditional Execution
#   - Conditional Value

if __name__ == '__main__':

    # Conditional Execution:
    a, b = 0, 1

    if a < b:
        print("a ({}) is less than b ({})".format(a, b))
    elif a > b:
        print("a ({}) is not less than b ({})".format(a, b))
    else:
        print("a ({}) is equal to b ({})".format(a, b))

    # Conditional Value:
    a, b = 0, 1
    s = "less than" if a < b else "not less than"

    print("a ({}) is {} b ({})".format(a, s, b))
