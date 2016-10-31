import _sqlite3


class Database:
    def __init__(self, db_name):
        self._properties = dict()
        self._properties['connection'] = _sqlite3.connect('db_name')
        self._properties['connection'].execute('DROP TABLE IF EXISTS test')
        self._properties['connection'].execute('CREATE TABLE test(t1 TEXT, i1 INT)')

    @property
    def connection(self):
        return self._properties['connection']


def main():
    db = Database('oop.db')


if __name__ == '__main__':
    main()
