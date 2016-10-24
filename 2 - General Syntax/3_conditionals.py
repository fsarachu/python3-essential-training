# There are two types of conditionals in python:
#   - Conditional Executions
#   - Conditional Values

if __name__ == '__main__':
    a, b = 0, 1

    if a < b:
        print("a ({}) is less than b ({})".format(a, b))
    elif a > b:
        print("a ({}) is not less than b ({})".format(a, b))
    else:
        print("a ({}) is equal to b ({})".format(a, b))
