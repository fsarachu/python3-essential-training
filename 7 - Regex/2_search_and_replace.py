import re

fh = open('raven.txt')

for line in fh.readlines():
    print(re.sub('((l|L)en|(N|n)everm)ore', '*****', line), end='')
