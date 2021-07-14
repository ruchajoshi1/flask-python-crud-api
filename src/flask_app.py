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
    #print(jsonify(widgets))
    return jsonify(widgets)
    #json_string = json.dumps([ob.__dict__ for ob in widgets])
    #return json_string

@app.route("/widget", methods=["GET", "POST"])
def insert_widget():
    if request.method == 'POST':
        widget_details = request.get_json()
        name = widget_details["name"]
        number_of_parts = widget_details["number_of_parts"]
        #name = request.form.get("name")
        #number_of_parts = int(request.form.get("number_of_parts"))
        created_date = date.today().strftime("%Y-%m-%d")
        updated_date = created_date
        widget_controller.create_widget(name, number_of_parts, created_date, updated_date)
        
        return "true"


@app.route("/widget", methods=["PUT"])
def update_widget():
    
    if request.method == 'PUT':
        widget_details = request.get_json()
        id = widget_details["id"]
        name = widget_details["name"]

        updated_date = date.today().strftime("%Y-%m-%d")
        #updated_date = datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
        widget_controller.update_widget(id, name, updated_date)
        
        return "true"

@app.route("/widget/<id>", methods=["DELETE"])
def delete_widget(id):
    widget_controller.delete_widget(id)
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