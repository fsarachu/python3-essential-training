def main():
    try:
        lines = read_file('lines.mp3')
        for line in lines:
            print(line, end='')
    except IOError as e:
        print('Couldn\'t open the file: {}'.format(e))
    except ValueError as e:
        print('Bad name: {}'.format(e))


def read_file(name):
    if name.endswith('.txt'):
        fh = open(name)
        return fh.readlines()
    else:
        raise ValueError('File name must end with ".txt"')


if __name__ == '__main__':
    main()
