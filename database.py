import sqlite3

# Opens a connection to the SQLite database and enforces foreign key constraints
def get_connection():
    conn = sqlite3.connect("food_inspection.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

# Reads Schema.sql and creates all tables in the database
def create_database():
    conn = get_connection()
    with open("Schema.sql","r") as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Food database ready.")
