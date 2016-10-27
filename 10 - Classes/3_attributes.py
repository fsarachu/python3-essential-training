class Duck:
    def __init__(self, **kwargs):
        self._name = kwargs.get('name', 'donald')

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def quack(self):
        print('{} quaaaackkks!'.format(self.get_name()))

    def walk(self):
        print('{} is walking!'.format(self.get_name()))


if __name__ == '__main__':
    lilly = Duck(name='Lilly')

    lilly.quack()
    lilly.walk()
