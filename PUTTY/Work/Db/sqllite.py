
import sqlite3

dbconn=sqlite3.connect('./testdb.db')
cursor=dbconn.cursor()

try:
	cursor.execute("CREATE TABLE if not exists user(id INTEGER, name text, phone text, gender text)")
	cursor.execute("INSERT INTO user(id, name,phone,gender) VALUES(1,'park','010','male')")
	cursor.execute("INSERT INTO user(id, name,phone,gender) VALUES(2,'park','010-2','female')")
	cursor.executemany("insert into user(id, name, phone, gender) values(?,?,?,?)",\
	[(3,'kim','010-3','f'),(4,'choi','010-4','m'),(5,'Lee','010-5','f')])
	dbconn.commit()
except KeyboardInterrupt:
	dbconn.close()

