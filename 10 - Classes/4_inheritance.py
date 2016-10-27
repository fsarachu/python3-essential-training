class Animal:
    def talk(self):
        print('I dont know what to say!')

    def walk(self):
        print('I\'m an animal walking')


class Duck(Animal):

    def talk(self):
        print('I cant talk, I only quack!')

    def quack(self):
        print('Quaaaackkk!')

    def walk(self):
        super().walk()
        print('I\'m also a duck walking!')


if __name__ == '__main__':
    lilly = Duck()

    lilly.talk()
    lilly.quack()
    lilly.walk()
