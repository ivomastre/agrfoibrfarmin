# connect_db.py
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database

    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement

    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
###

def select_cidade(conn,cidadeNome):
    sql = """SELECT * FROM tempo WHERE cidadeNome = "?"
        """.replace("?", cidadeNome,1)
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()
    #return rows
    for row in rows:
        #print(row) #tuple
        print("ID: ", row[0])
        print("Nome: " + row[1])
        print("Temperatura: "+ row[2])
        print("\n")

def create_tempo(conn, cidadeNome,tempMax, tempMin,umidadeMin, umidadeMax):
    """
    Create a new project into the tempo table

    """
    sql = """ INSERT INTO tempo(cidadeNome,tempMin, tempMax, umidadeMin, umidadeMax)
                  VALUES('?','?', '?', '?', '?') """.replace("?", cidadeNome, 1 ).replace("?", tempMin, 1).replace("?", tempMax, 1).replace("?", umidadeMin, 1).replace("?", umidadeMax, 1)
    print(sql)
    cur = conn.cursor()
    cur.execute(sql)
    print("executei")
    conn.commit()
    cur.close()

def select_all_tempo(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tempo")
        rows = cur.fetchall()
        conn.close()
        return rows
    else:
        print("Error! cannot create the database connection.")
def main():
    database = "D:\\sqlite\db\pythonsqlite.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS tempo(
                                        id integer PRIMARY KEY,
                                        cidadeNome text NOT NULL,
                                        tempMin text,
                                        tempMax text,
                                        umidadeMin text, 
                                        umidadeMax text
                                    ); """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
        # create tasks table
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()