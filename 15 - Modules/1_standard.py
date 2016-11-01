import sys


def main():
    print('Python version: {}.{}.{}'.format(*sys.version_info))
    print('Platform: {}'.format(sys.platform))

    import os

    print('os name: {}'.format(os.name))
    print('PATH variable: {}'.format(os.getenv('PATH')))
    print('cwd: {}'.format(os.getcwd()))


if __name__ == '__main__':
    main()
