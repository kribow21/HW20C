from flask import Flask, request, Response

app=Flask(__name__)

@app.route('/animals')
def animal_manip():
    return 'Hello'