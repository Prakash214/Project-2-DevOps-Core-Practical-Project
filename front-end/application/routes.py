from application import app
import requests
from flask import render_template, url_for, jsonify

@app.route('/')
def index():
    fruit_ = requests.get('http://fruit:5000/get-fruit')
    friend_ = requests.get('http://friend:5000/get-friend')
    characters_ = requests.post('http://characters:5000/get-characters', json=fruit_.json())
    return render_template('index.html',character=characters_.json()['character'], fruit=fruit_.json()['fruit'], friend=friend_.json()['friend'])