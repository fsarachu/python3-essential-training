try:
    fh = open('lines.txt')
    for line in fh.readlines():
        print(line, end='')
except IOError as e:
    print('Error handling the file: {}'.format(e))
