class Duck:
    def __init__(self, name):
        self.name = name

    def quack(self):
        print('{} quaaaackkks!'.format(self.name))

    def walk(self):
        print('{} is walking!'.format(self.name))


if __name__ == '__main__':
    lilly = Duck('Lilly')

    lilly.quack()
    lilly.walk()
