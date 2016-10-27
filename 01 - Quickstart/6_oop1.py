class Fibonacci:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while True:
            yield self.b
            self.a, self.b = self.b, self.a + self.b


f = Fibonacci(0, 1)

for x in f.series():
    if x > 100:
        break
    print(x)
