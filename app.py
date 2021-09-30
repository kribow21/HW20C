from flask import Flask, request, Response
import json

app=Flask(__name__)

@app.route('/animals', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def animal_manip():
    if request.method == 'GET':
        params = request.args
        animal_dict = {
            "animal" : "horse",
            "animal" : "pig",
            "animal" : "cow",
            "animal" : "moose",
            "animal" : "beaver",
            "animal" : "squirrel",
        }
        for animal in animal_dict:
            print(animal)
        print(params)
        return Response(json.dumps(animal_dict, default=str),
                        mimetype="application/json",
                        status=200)
    elif request.method == 'POST':
        data = request.json
        add_animal = {
            "animal" : "monkey"
        }
        print(data)
        return Response ("Added an animal to the list",
                        mimetype="text/html",
                        status=200)
    elif request.method == 'PATCH':
        data = request.json
        edit_animal = {
            "animal" : "fluffy squirrel"
        }
        print(data)
        return Response ("Edited an animal in the list",
                        mimetype="text/html",
                        status=200)
    elif request.method == 'DELETE':
        data = request.json
        delete_animal = {
            "animal" : "cow"
        }
        print(data)
        return Response ("Deleted an animal from the list",
                        mimetype="text/html",
                        status=200)
    else:
        print("Something wrong, flask let bad request through")