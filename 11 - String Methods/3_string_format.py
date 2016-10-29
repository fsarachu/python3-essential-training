a, b = 5, 42

s1 = 'a is {0}, b is {1}, again a is {0}'

print(s1.format(a, b))

s2 = 'first is {bob}, second is {fred}'

names = dict(bob='bobby', fred='freddy')

print(s2.format(**names))
