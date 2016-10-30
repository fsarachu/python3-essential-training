import _sqlite3

db = _sqlite3.connect('test.db')

db.execute('DROP TABLE IF EXISTS test')
db.execute('CREATE TABLE test(t1 TEXT, i1 INT)')

values = dict(one=1, two=2, three=3, four=4)

for k in values:
    db.execute('INSERT INTO test (t1, i1) VALUES (?, ?)', (k, values[k]))

db.commit()

cursor = db.execute('SELECT * FROM test ORDER BY i1')

for row in cursor:
    print(row)
