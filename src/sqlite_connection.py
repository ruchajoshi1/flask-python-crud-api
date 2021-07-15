# -*- coding: utf-8 -*-
'''
    sqlite_connection.py - this file contains sqlite connection and 
    table creation method
'''

import sqlite3
from sqlite3 import Error

DATABASE_NAME = r"../db/pythonsqlite.db"


# create sqlite connection
def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
    except Error as e:
        print(e)
    
    return conn


# create widgets table
def create_table():
    """ create a table from the create_table_sql statement """    
    try:
        create_table_sql = """ CREATE TABLE IF NOT EXISTS widgets (
                                        id integer PRIMARY KEY,
                                        name text(64) NOT NULL,
                                        number_of_parts integer, 
                                        created_date text,
                                        updated_date text
                                    ); """
        conn = create_connection()    
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
