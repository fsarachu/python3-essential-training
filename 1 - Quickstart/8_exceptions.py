try:
    fh = open("xlines.txt")
    for line in fh.readlines():
        print(line)
except:
    print("something went wrong while reading the file")
