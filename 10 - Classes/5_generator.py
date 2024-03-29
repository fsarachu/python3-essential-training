class InclusiveRange:
    def __init__(self, *args):
        arg_count = len(args)

        if arg_count < 1:
            raise TypeError('At least 1 argument is expected')
        elif arg_count == 1:
            self.start = 0
            self.stop = args[0]
            self.steps = 1
        elif arg_count == 2:
            self.start, self.stop = args
            self.steps = 1
        elif arg_count == 3:
            self.start, self.stop, self.steps = args
        else:
            raise TypeError('Too many arguments, at most 3 are spected, got {}'.format(arg_count))

    def __iter__(self):
        i = self.start

        while i <= self.stop:
            yield i
            i += self.steps


def main():
    o1 = InclusiveRange(15)
    o2 = InclusiveRange(5, 15)
    o3 = InclusiveRange(5, 15, 3)

    for i in o1:
        print(i, end=' ')

    print("\n------------------")

    for i in o2:
        print(i, end=' ')

    print("\n------------------")

    for i in o3:
        print(i, end=' ')

    print("\n------------------")


if __name__ == '__main__':
    main()
