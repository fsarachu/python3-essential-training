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

    # In an assignment statement, the right-hand side is always evaluated fully
    # before doing the actual setting of variables. In this case it swaps 'a' and 'b'

    a, b = b, a
    print("a: {}".format(a))
    print("b: {}".format(b))

    print("---------------------")

    a = (1, 2, 3, 4, 5)  # Parentheses defines a tuple
    print(a)


if __name__ == '__main__':
    main()
