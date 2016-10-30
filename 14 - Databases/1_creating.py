import _sqlite3

db = _sqlite3.connect('test.db')

db.execute('DROP TABLE IF EXISTS test')
db.execute('CREATE TABLE test(t1 TEXT, i1 INT)')
