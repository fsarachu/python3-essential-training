import _sqlite3


def insert(db, row):
    db.execute('INSERT INTO test (t1, i1) VALUES (?, ?)', (row['t1'], row['i1']))
    db.commit()


def retrieve(db, t1):
    cursor = db.execute('SELECT * FROM test WHERE t1 = ?', (t1,))
    return cursor.fetchone()


def update(db, row):
    db.execute('UPDATE test SET i1 = ? WHERE t1 = ?', (row['i1'], row['t1']))
    db.commit()


def delete(db, t1):
    db.execute('DELETE FROM test WHERE t1 = ?', (t1,))
    db.commit()


def disp_rows(db):
    cursor = db.execute('SELECT * FROM test ORDER BY t1')
    for row in cursor:
        print('{}: {}'.format(row['t1'], row['i1']))


def main():
    db = _sqlite3.connect('test.db')


if __name__ == '__main__':
    main()
