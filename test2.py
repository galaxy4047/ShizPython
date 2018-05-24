import sqlite3 as lite
con=lite.connect('Drive.db')
with con:
	cur=con.cursor()
	rows=cur.execute("select * from Driver ")
	for row in rows:
		print row
