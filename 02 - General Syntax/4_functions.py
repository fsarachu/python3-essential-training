def main():
    func()
    func_with_parameter(3)
    func_with_parameter_and_default_value()


def func():
    print("This is a function!")


def func_with_parameter(a):
    for i in range(a, 10):
        print(i, end=' ')
    print('')


def func_with_parameter_and_default_value(a=0):
    for i in range(a, 10):
        print(i, end=' ')
    print('')


if __name__ == '__main__':
    main()
