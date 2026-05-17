import sqlite3
#used to test to see if database is connected
conn = sqlite3.connect("food_inspection.db")
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print(tables)
conn.close()
