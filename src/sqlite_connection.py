# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error

DATABASE_NAME = r"C:\Users\mvjos\AWeber_Assignment\db\pythonsqlite.db"


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
    except Error as e:
        print(e)
    
    return conn


def create_table():
    """ create a table from the create_table_sql statement """
    
    try:
        create_table_sql = """ CREATE TABLE IF NOT EXISTS widgets (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        number_of_parts integer, 
                                        created_date text,
                                        updated_date text
                                    ); """

        # create a database connection
        conn = create_connection()
    
        c = conn.cursor()
        c.execute(create_table_sql)
        #print("Widget table created.")
    except Error as e:
        print(e)
