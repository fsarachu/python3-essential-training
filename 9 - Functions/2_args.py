def main():
    some_function(1, 2, 3, 4, 5, 6, 7)


def some_function(a, b, c, *args):
    print('a: {}, b: {}, c: {}'.format(a, b, c))

    print('others: ', end='')
    for n in args:
        print(n, end=' ')


if __name__ == '__main__':
    main()
