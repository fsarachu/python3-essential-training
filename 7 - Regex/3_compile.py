import re

fh = open('raven.txt')
regex = re.compile('((l|L)en|(N|n)everm)ore')

for line in fh.readlines():
    match = re.search(regex, line)
    if match:
        print(line, end='')
