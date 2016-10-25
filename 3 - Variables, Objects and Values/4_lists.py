# A list is mutable, but less efficient than a tuple

# Some list methods
a = [66.25, 333, 333, 1, 1234.5]
print("Initial list: {}".format(a))
print("count(333): {}, count(66.25): {}, count('x'): {} ".format(a.count(333), a.count(66.25), a.count('x')))

a.insert(2, -1)
a.append(333)
print("After insert(2, -1) and append(333): {}".format(a))

print("index(333): {}".format(a.index(333)))

a.remove(333)
print("After remove(333): {}".format(a))

a.reverse()
print("After reverse(): {}".format(a))

a.sort()
print("After sort(): {}".format(a))

print("pop(): {}".format(a.pop()))
print("After pop(): {}".format(a))
