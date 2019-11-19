import sqlite3 
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        

def mainDb():
    database = r"./myGameDb.db"
 
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        value text NOT NULL
                                    );"""
 
    # create a database connection
    conn = create_connection(database)
 
    # create tables
    if conn is not None:
        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")
 
def create_name_value_pair(name, value):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
 
    database = r"./myGameDb.db"
    conn=create_connection(database)
    sql = ''' INSERT INTO tasks(name,value)
              VALUES(?,?) '''
    pair=(name,value)
    with conn:
        cur = conn.cursor()
        cur.execute(sql, pair)
        print(str(cur.lastrowid))
        print(pair)
