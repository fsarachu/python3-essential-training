buffersize = 5000

infile = open('bigfile.txt', 'r')
outfile = open('bigoutput.txt', 'w')

buffer = infile.read(buffersize)

print('Writing to \'{}\'...'.format(outfile.name))

while len(buffer):
    print('.', end='')
    outfile.write(buffer)
    buffer = infile.read(buffersize)

print('\n')
print('Done!')
