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
            self.start = args[0]
            self.stop = args[1]
            self.steps = 1
        elif arg_count == 3:
            self.start = args[0]
            self.stop = args[1]
            self.steps = args[2]
        else:
            raise TypeError('Too many arguments, at most 3 are spected, got {}'.format(arg_count))

    def __iter__(self):
        pass


def main():
    o = range(25)

    for i in o:
        print(i, end=' ')


if __name__ == '__main__':
    main()
