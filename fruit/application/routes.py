from application import app
import requests
from flask import jsonify
from random import choice

fruits = ["Dark-Dark Fruit","Soul-Soul Fruit","Tremor-Tremor Fruit","Fish-Fish Fruit",]

@app.route('/get-fruit', methods=['GET'])
def get_fruit():
    fruit = choice(fruits)
    return jsonify(fruit=fruit)