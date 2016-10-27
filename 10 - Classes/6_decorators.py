class Duck:
    def __init__(self, **kwargs):
        self.properties = dict()
        self.properties['name'] = kwargs.get('name', 'Anonymous Duck')

    def quack(self):
        print('{} quaaaackkks!'.format(self.properties['name']))

    def walk(self):
        print('{} is walking!'.format(self.properties['name']))

    @property
    def name(self):
        return self.properties.get('name', None)

    @name.setter
    def name(self, n):
        self.properties['name'] = n

    @name.deleter
    def name(self):
        del self.properties['name']


if __name__ == '__main__':
    lilly = Duck()

    print(lilly.name)

    lilly.name = 'Lilly'

    print(lilly.name)
