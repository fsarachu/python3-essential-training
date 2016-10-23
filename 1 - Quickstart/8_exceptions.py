try:
    fh = open("xlines.txt")
    for line in fh.readlines():
        print(line)
except IOError as e:
    print("something went wrong: {}".format(e))

print("After badness")  # Execution continues after handled error
