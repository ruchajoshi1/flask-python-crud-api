### flask-python-crud-api

This project is a CRUD REST API using python, Flask and SQLite.
This is written in Python 3.8.
There are endpoints to create, read, list, update and delete objects called 
"Widgets".

*Widget object includes following properties - 
Id,
Name,
Number of parts,
Created date,
Updated date

Widgets are persisted to and retrieved from a SQLite database.

To run the api please follow below steps - 
1. Navigate to the file named as main.py. This is located at 
flask-python-crud-api/src/main.py
Choose "Run As"
Choose "Python Run"
This will start the api.

2. To test different CRUD operations run below commands on command window

* Create - 'curl -X POST -H "Content-Type: application/json" --data @new_rec.json http://localhost:8000/widget'
  This will add a new widget to a database. new_rec.json needs to be updated
  with the required information.

* Read - 'curl -X GET http://localhost:8000/widgets' 
  This will print the list of all the widgets available in the database.

* Read by id - 'curl -X GET http://localhost:8000/widget/{id}' 
  Pass the id go retrieve required data

* Update - 'curl -X PUT -H "Content-Type: application/json" --data @update_rec.json http://localhost:8000/widget'
  This will update the record for a given Id. We need to pass the values 
  in the update_rec.json.

* Delete - 'curl -X DELETE http://localhost:8000/widget/{id}'
  This will delete the corresponding data for the provided id from the database.