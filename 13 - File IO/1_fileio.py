infile = open('lines.txt', 'r')
outfile = open('output.txt', 'w')

for index, line in enumerate(infile):
    print('Index: {}, Line Content: {}'.format(index, line), file=outfile, end='')
