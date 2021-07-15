# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, json, url_for
import widget_controller
from sqlite_connection import create_table
from datetime import date, datetime

#creating  a flask instance
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/widgets', methods=["GET"])
def get_all_widgets():
    widgets = widget_controller.select_all_widgets()
    return jsonify(widgets)


@app.route("/widget", methods=["GET", "POST"])
def insert_widget():
    if request.method == 'POST':
        widget_details = request.get_json()
        name = widget_details.get("name")
        number_of_parts = widget_details.get("number_of_parts")
        if (name is None) or (number_of_parts is None):
            return jsonify({'Status':'Error','Output':'Either name or number_of_parts is not specified in the json object'})
        else:
            created_date = date.today().strftime("%Y-%m-%d")
            updated_date = created_date
            return_dict = widget_controller.create_widget(name, number_of_parts, created_date, updated_date)
            return jsonify(return_dict)


@app.route("/widget", methods=["PUT"])
def update_widget():
    
    if request.method == 'PUT':
        widget_details = request.get_json()
        id = widget_details.get("id")
        name = widget_details.get("name")
        
        if (id is None) or (name is None):
            return jsonify({'Status':'Error','Output':'Either id or name is not specified in the json object'})
        else:
            updated_date = date.today().strftime("%Y-%m-%d")
            #updated_date = datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
            num_rows = widget_controller.update_widget(id, name, updated_date)
            if num_rows > 0:
                return jsonify({'Status':'Success', 'Output': 'Updated record for id {} '.format(id) })
            else:
                return jsonify({'Status':'Error', 'Output': 'No records found for id {}'.format(id)})

@app.route("/widget/<id>", methods=["DELETE"])
def delete_widget(id):
    num_rows=widget_controller.delete_widget(id)
    if num_rows > 0:
        return jsonify({'Status':'Success', 'Output': 'Deleted record for id {} '.format(id) })
    else:
        return jsonify({'Status':'Error', 'Output': 'No records found for id {}'.format(id)})

    
    return ''' Deleted record {}'''.format(id)



@app.route("/widget/<id>", methods=["GET"])
def get_by_id(id):
    widget = widget_controller.get_widget_by_id(id)
    return jsonify(widget)



# favicon
@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='/images/my_favicon.png')


if __name__ == "__main__":
    
    # create table
    create_table()
        
    app.run(host='localhost', port=8000, debug=False)