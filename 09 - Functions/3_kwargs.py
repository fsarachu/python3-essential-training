def main():
    some_function(one=23, two=76, five=0)


def some_function(**kwargs):
    for k in kwargs:
        print('{}: {}'.format(k, kwargs[k]))


if __name__ == '__main__':
    main()
