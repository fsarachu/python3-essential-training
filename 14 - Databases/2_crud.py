import _sqlite3


def insert(db, row):
    db.execute('INSERT INTO test (t1, i1) VALUES (?, ?)', (row['t1'], row['i1']))
    db.commit()


def retrieve(db, t1):
    cursor = db.execute('SELECT * FROM test WHERE t1 = ?', (t1,))
    return cursor.fetchone()


def main():
    db = _sqlite3.connect('test.db')


if __name__ == '__main__':
    main()
