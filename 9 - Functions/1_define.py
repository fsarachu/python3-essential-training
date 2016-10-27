def main():
    some_function(c=10)


def some_function(a=0, b=None, c=0):
    if b is None:
        b = 0

    print('This is a function')
    print('a: {}, b: {}, c: {}'.format(a, b, c))


if __name__ == '__main__':
    main()
