import sqlite3
con = sqlite3.connect("mydatabase.db")
cur = con.cursor()
cur.execute('''CREATE TABLE balance (name text, balance text)''')
