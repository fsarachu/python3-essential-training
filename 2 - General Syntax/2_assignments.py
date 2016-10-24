def main():
    a = 1
    b = "Hello"
    print(type(a), a)
    print(type(b), b)
    c = None  # Python's Null equivalent
    print(type(c), c)

    print("---------------------")

    a, b = 0, 1
    print("a: {}".format(a))
    print("b: {}".format(b))

    print("---------------------")

    a, b = b, a
    print("a: {}".format(a))
    print("b: {}".format(b))

    print("---------------------")


if __name__ == '__main__':
    main()
