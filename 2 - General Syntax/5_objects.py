class Egg:
    def __init__(self, type="Fried"):
        self.type = type

    def get_type(self):
        return self.type

def main():
    fried = Egg()


if __name__ == '__main__':
    main()
