import sys


def main():
    print('Python version: {}.{}.{}'.format(*sys.version_info))
    print('Platform: {}'.format(sys.platform))

    import os

    print('os name: {}'.format(os.name))
    print('PATH variable: {}'.format(os.getenv('PATH')))
    print('cwd: {}'.format(os.getcwd()))
    print('urandom; {}'.format(os.urandom(25)))

    import urllib.request

    page = urllib.request.urlopen('https://webapp2.readthedocs.io/en/latest/')

    # for line in page:
    #     print(str(line, encoding='utf_8'), end='')

    import random

    for i in range(10):
        print(random.randint(1, 100), end=' ')

    print()


if __name__ == '__main__':
    main()
