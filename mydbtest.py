import sqlite3

conn = sqlite3.connect('mynewsql.db')

cur = conn.cursor()

#cur.execute('CREATE TABLE STUDENT(SID INT, SNAME VARCHAR(20))')

conn.commit()

cur.execute("insert into student values (1, 'sanjay')")
conn.commit()