import sys


def main():
    print('Python version: {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import os

    print(os.name)
    print(os.getenv('PATH'))


if __name__ == '__main__':
    main()
