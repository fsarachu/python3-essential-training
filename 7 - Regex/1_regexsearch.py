import re

fh = open('raven.txt')

for line in fh.readlines():
    if re.search('((l|L)en|(N|n)everm)ore', line):
        print(line, end='')
