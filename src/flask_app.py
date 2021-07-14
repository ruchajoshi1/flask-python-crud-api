# -*- coding: utf-8 -*-

#import os
#print("Current Working Directory", os.getcwd())

from flask import Flask, jsonify, request, json, url_for
import widget_controller
from sqlite_connection import create_table
from datetime import date

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


# # allow both GET and POST requests
# @app.route('/form-example', methods=['GET', 'POST'])
# def form_example():
#     # handle the POST request
#     if request.method == 'POST':
#         language = request.form.get('language')
#         framework = request.form.get('framework')
#         return '''
#                   <h1>The language value is: {}</h1>
#                   <h1>The framework value is: {}</h1>'''.format(language, framework)

#     # otherwise handle the GET request
#     return '''
#            <form method="POST">
#                <div><label>Language: <input type="text" name="language"></label></div>
#                <div><label>Framework: <input type="text" name="framework"></label></div>
#                <input type="submit" value="Submit">
#            </form>'''


@app.route("/widget-create", methods=["GET", "POST"])
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
        
    #return jsonify(result)
    # return '''
    #         <form method="POST">
    #            <div><label>Name: <input type="text" name="name"></label></div>
    #            <div><label>Number of parts: <input type="text" name="number_of_parts"></label></div>
    #            <input type="submit" value="Submit">
    #        </form>'''
    


@app.route("/widget-update", methods=["PUT"])
def update_widget():
    
    if request.method == 'PUT':
        widget_details = request.get_json()
        id = widget_details["id"]
        name = widget_details["name"]
        #id = request.form.get("id")
        #name = request.form.get("name")
        updated_date = date.today().strftime("%Y-%m-%d")
        widget_controller.update_widget(id, name, updated_date)
    # return '''
    #         <form method="PUT">
    #             <div><label>Id: <input type="text" name="Id"></label></div>
    #             <div><label>Name: <input type="text" name="name"></label></div>               
    #            <input type="submit" value="Submit">
    #        </form>'''


@app.route("/widget-delete/<id>", methods=["DELETE"])
def delete_widget(id):
    widget_controller.delete_widget(id)
    return ''' Deleted record {}'''.format(id)



@app.route("/widget/<id>", methods=["GET"])
def get_by_id(id):
    widget = widget_controller.get_widget_by_id(id)
    return jsonify(widget)

# @app.errorhandler(404)
# def not_found(error=None):
#     message = {
#         'status': 404,
#         'message': 'Not found: ' + request.url,
#         }
    
#     resp = jsonify(message)
#     resp.status.node = 404
    
#     return resp

# favicon
@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='/images/my_favicon.png')


if __name__ == "__main__":
    
    # create table
    create_table()
        
    app.run(host='localhost', port=8000, debug=False)