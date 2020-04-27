from flask import Flask, request
import enum 
import json


app = Flask(__name__)


dictionary = {} 
unique_id = 0

#create a new task 
@app.route('/v1/tasks', methods = ['POST'])
def post():
    global unique_id
    data = request.get_json()
    value = [data["title"], False]
    if len(dictionary) == 0: 
        unique_id = 1 
        dictionary[unique_id] = value
    else: 
        dictionary[unique_id] = value
    
    unique_id += 1

    response = {
        "id": unique_id
    }

    
    return json.dumps(response), 201

# #all multiple tasks 
# @app.route('/v1/tasks', methods = ['POST'])
# def post():
#     data = request.get_json()
#     tasks = data['tasks']
#     unique_numbers = [] 

#     if len(dictionary) == 0: 
#         unique_id = 1 
    
#     for task in tasks:
#         dictionary[unique_id] = [task['title'], task['is_completed']]
#         unique_numbers.append(unique_id)
#         unique_id += 1

#     response = [] 

#     for n in unique_numbers:
#         id_dict = {'id' : n}
#         response.append(id_dict)
#     response = {'tasks': response}
#     return json.dumps(response), 201


@app.route('/v1/tasks', methods = ['GET'])
def get_all_tasks():
    created_tasks = [] 

    for id in dictionary:
        res = {'id' : id, 'title': dictionary[id][0], 'is_completed': dictionary[id][1]}
        created_tasks.append(res)

    response = {"tasks" : created_tasks}
    return json.dumps(response), 200


@app.route('/v1/tasks/<id>', methods = ['GET'])
def get_2(id):
    id = int(id)
    if id in dictionary:
        response = {"id" : id, 'title': dictionary[id][0], 'is_completed': dictionary[id][1]}
        return json.dumps(response), 200
    else: 
        response = {'error': "There is no task at that id"}
        return json.dumps(response), 404

@app.route('/v1/tasks/<id>', methods = ['DELETE'])
def delete_2(id):
    id = int(id)
    if id in dictionary:
        del dictionary[id]
    response = None
    return json.dumps(response), 204

# @app.route('/v1/tasks/<id>', methods = ['DELETE'])
# def delete_2(id):
#     data = request.get_json()
#     ids = data['tasks']
#     for item in ids:
#         del dictionary[int(item['id'])]
#     response = None
#     return json.dumps(response), 204


@app.route('/v1/tasks/<id>', methods = ['PUT'])
def put(id):
    data = request.get_json()
    if data is None:
        return json.dumps(None)
    else: 
        id = int(id)
        if id in dictionary:
            dictionary[id] = [data['title'], data['is_completed']]
            return json.dumps(None), 204
        else:
            response = {'error': 'There is no task at that id'}
            return json.dumps(response), 404

    
        


