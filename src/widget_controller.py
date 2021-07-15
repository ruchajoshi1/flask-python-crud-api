# -*- coding: utf-8 -*-

import sqlite3
from sqlite_connection import create_connection

def create_widget(name, number_of_parts, created_date, updated_date):
    """
    Create a new widget into the widgets table
    :param name:
    :param number_of_parts:
    :param created_date:
    :param updated_date:
    :return: None
    """
    conn = create_connection()
    sql = ''' INSERT INTO widgets(name,number_of_parts,created_date,updated_date)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (name, number_of_parts, created_date, updated_date))
    conn.commit()
    #return(cur.rowcount)
    return_dict = {}
    if (cur.rowcount > 0):
        return_dict['Status'] = "Success"
        return_dict['Output'] = "Record inserted"
        return_dict['id'] = cur.lastrowid
    else:
        return_dict['Status'] = "Error"
        return_dict['Output'] = "No records inserted"
        return_dict['id'] = ''
    return(return_dict)
        
        
    


def select_all_widgets():
    """
    Query all rows in the widgets table
    :param:
    :return:
    """
    conn = create_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM widgets").fetchall()
    list_dict = []
    return_dict = {}
    if (rows is None) or len(rows) <= 0:
        return_dict['Status'] = "Error"
        return_dict['Output'] = "No rows returned from the database"
    else:
        for row in rows:
            list_dict.append(dict(row))
        return_dict['Status'] = 'Success'
        return_dict['Output'] = list_dict
    
    return return_dict

    
        
def get_widget_by_id(id):
    """
    Query widgets table by id and return a widget
    :param id: 
    :return :
    """
    conn = create_connection()
    conn.row_factory = sqlite3.Row
    sql = ''' SELECT * FROM widgets WHERE id = {}'''.format(id)
    cur = conn.cursor()
    cur.execute(sql)
    
    row = cur.fetchone()
    return_dict = {}
    if row==None:
        return_dict['Status'] = "Error"
        return_dict['Output'] = 'No data returned while searching for id {}'.format(id)
    else:
        return_dict['Status'] = 'Success'
        return_dict['Output'] = dict(row)
    return return_dict
    

def update_widget(id, name, updated_date):
    """
    update name, and updated_date of a widget in widgets table
    :param conn:
    :param widget:
    :return:
    """
    conn = create_connection()
    sql = ''' UPDATE widgets set name="{}", updated_date="{}" where id={} '''.format(name,updated_date,id)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    num_rows = cur.rowcount
    return num_rows


def delete_widget(id):
    """
    Delete a widget by widget id
    :param conn:  Connection to the SQLite database
    :param id: id of the widget
    :return:
    """
    conn = create_connection()
    sql = '''DELETE FROM widgets WHERE id={}'''.format(id)
    cur = conn.cursor()
    cur.execute(sql) 
    conn.commit()
    num_rows = cur.rowcount
    return num_rows

