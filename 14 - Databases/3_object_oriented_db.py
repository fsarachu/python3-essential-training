import _sqlite3


class Database:
    def __init__(self, db_name):
        self._properties = dict()
        self._properties['connection'] = _sqlite3.connect(db_name)
        self._properties['connection'].execute('DROP TABLE IF EXISTS test')
        self._properties['connection'].execute('CREATE TABLE test(t1 TEXT, i1 INT)')

    @property
    def connection(self):
        return self._properties['connection']

    def sql(self, sql_string, commit=True):
        """Executes 'sql_string' exactly as received and commits changes automatically"""

        result = self.connection.execute(sql_string)

        if commit:
            self.connection.commit()

        return result


def main():
    db = Database('oop.db')
    db.sql('INSERT INTO test (t1, i1) VALUES ("one", 1)')


if __name__ == '__main__':
    main()
