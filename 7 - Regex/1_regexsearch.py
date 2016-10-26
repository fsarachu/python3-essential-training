import re

fh = open('raven.txt')

for line in fh.readlines():
    match = re.search('((l|L)en|(N|n)everm)ore', line)
    if match:
        print(match.group())
