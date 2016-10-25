# A list is mutable, but less efficient than a tuple

print("\n--- Some List Methods ---")

a = [66.25, 333, 333, 1, 1234.5]
print("a: {}".format(a))
print("a.count(333): {}, a.count(66.25): {}, a.count('x'): {} ".format(a.count(333), a.count(66.25), a.count('x')))

a.insert(2, -1)
a.append(333)
print("a.insert(2, -1) and a.append(333): {}".format(a))

print("a.index(333): {}".format(a.index(333)))

a.remove(333)
print("a.remove(333): {}".format(a))

a.reverse()
print("a.reverse(): {}".format(a))

a.sort()
print("a.sort(): {}".format(a))

print("a.pop(): {}".format(a.pop()))
print("After a.pop(): {}".format(a))

print("\n--- Lists as Stacks ---")

stack = [1, 2, 3]
print("stack: {}".format(stack))

stack.append(4)
print("stack.append(4): {}".format(stack))

stack.append(5)
print("stack.append(5): {}".format(stack))

print("stack.pop(): {}".format(stack.pop()))
print("stack.pop(): {}".format(stack.pop()))
print("stack.pop(): {}".format(stack.pop()))

print("stack: {}".format(stack))
