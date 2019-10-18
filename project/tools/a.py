from sqlite3 import Error
import sqlite3

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

if __name__ == '__main__':
    create_connection("D:\\sqlite\db\pythonsqlite.db")