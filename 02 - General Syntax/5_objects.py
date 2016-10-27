class Egg:
    def __init__(self, type="Fried"):
        self.type = type

    def get_type(self):
        return self.type


def main():
    fried = Egg()
    scrambled = Egg("Scrambled")

    print(fried.get_type())
    print(scrambled.get_type())


if __name__ == '__main__':
    main()
