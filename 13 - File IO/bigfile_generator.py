outfile = open('bigfile.txt', 'w')

for i in range(50000):
    print('{0:0>5} This is going to be a big file of useless text.'.format(i + 1), file=outfile)
