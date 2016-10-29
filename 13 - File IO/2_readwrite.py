infile = open('bigfile.txt', 'r')
outfile = open('bigoutput.txt', 'w')

print('Writing to \'{}\'...'.format(outfile))

for index, line in enumerate(infile):
    print('Index: {}, Line Content: {}'.format(index, line), file=outfile, end='')

print('Done!')
