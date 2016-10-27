def main():
    for n in inclusive_range(3, 9):
        print(n, end=' ')


def inclusive_range(start, stop, steps=1):
    i = start

    while i <= stop:
        yield i
        i += steps


if __name__ == '__main__':
    main()
