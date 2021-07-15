# -*- coding: utf-8 -*-
'''
    This is widget controller where CRUD methods are defined
'''

import sqlite3
from sqlite_connection import create_connection


# create widget - post request
def create_widget(name, number_of_parts, created_date, updated_date):
    """
    Create a new widget into the widgets table
    :param: name:
    :param: number_of_parts:
    :param: created_date:
    :param: updated_date:
    :return: return_dict:
    """
    conn = create_connection()
    sql = ''' INSERT INTO widgets(name,number_of_parts,created_date,updated_date)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (name, number_of_parts, created_date, updated_date))
    conn.commit()
    return_dict = {}
    if cur.rowcount > 0:
        return_dict['Status'] = "Success"
        return_dict['Output'] = "Record inserted"
        return_dict['id'] = cur.lastrowid
    else:
        return_dict['Status'] = "Error"
        return_dict['Output'] = "No records inserted"
        return_dict['id'] = ''
    return return_dict


# get method  - to retrieve all widgets
def select_all_widgets():
    """
    Query all rows in the widgets table
    :param:
    :return: return_dict
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


# get method - get widget by id
def get_widget_by_id(widget_id):
    """
    Query widgets table by id and return a widget
    :param widget_id:
    :return: return_dict
    """
    conn = create_connection()
    conn.row_factory = sqlite3.Row
    sql = ''' SELECT * FROM widgets WHERE id = {}'''.format(widget_id)
    cur = conn.cursor()
    cur.execute(sql)
    row = cur.fetchone()
    return_dict = {}
    if row is None:
        return_dict['Status'] = "Error"
        return_dict['Output'] = 'No data returned while searching for id {}'.format(widget_id)
    else:
        return_dict['Status'] = 'Success'
        return_dict['Output'] = dict(row)

    return return_dict


# put method - update widget by id
def update_widget(widget_id, name, updated_date):
    """
    update name, and updated_date of a widget in widgets table
    :param widget_id:
    :param: name:
    :param: updated_date:
    :return: num_rows:
    """
    conn = create_connection()
    sql = ''' UPDATE widgets set name="{}", updated_date="{}" where id={} '''.format(name,updated_date,widget_id)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    num_rows = cur.rowcount

    return num_rows


# delete method - delete widget by id
def delete_widget(widget_id):
    """
    Delete a widget by widget id
    :param: widget_id
    :return: num_rows
    """
    conn = create_connection()
    sql = '''DELETE FROM widgets WHERE id={}'''.format(widget_id)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    num_rows = cur.rowcount

    return num_rows
