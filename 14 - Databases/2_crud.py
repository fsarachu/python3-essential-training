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


def display_rows(db):
    cursor = db.execute('SELECT * FROM test ORDER BY t1')
    for row in cursor:
        print('{}: {}'.format(row['t1'], row['i1']))


def main():
    db = _sqlite3.connect('test.db')
    db.row_factory = _sqlite3.Row
    db.execute('DROP TABLE IF EXISTS test')
    db.execute('CREATE TABLE test(t1 TEXT, i1 INT)')

    print('Create rows')
    insert(db, dict(t1='one', i1=1))
    insert(db, dict(t1='two', i1=2))
    insert(db, dict(t1='three', i1=3))
    insert(db, dict(t1='four', i1=4))
    display_rows(db)

    print('Retrieve rows')
    print(dict(retrieve(db, 'one')), dict(retrieve(db, 'two')))


if __name__ == '__main__':
    main()
