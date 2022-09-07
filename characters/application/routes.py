from application import app
import requests
from flask import request, jsonify
from random import choice


@app.route('/get-characters', methods=['POST'])
def get_character():
    request_json = request.get_json()
    request_ = request_json['fruit']
    characters = ['big mom','kaidou','whitebeard','blackbeard']
    if request_ == "Dark-Dark Fruit":
        characters.append('blackbeard')
        characters.append('blackbeard')
        characters.append('blackbeard')
        characters.append('blackbeard')
    elif request_ == "Soul-Soul Fruit":
        characters.append('big mom')
        characters.append('big mom')
        characters.append('big mom')
        characters.append('big mom')
    elif request_ == "Tremor-Tremor Fruit":
        characters.append('whitebeard')
        characters.append('whitebeard')
        characters.append('whitebeard')
        characters.append('whitebeard')
    elif request_ == 'Fish-Fish Fruit':
        characters.append('kaidou')
        characters.append('kaidou')
        characters.append('kaidou')
        characters.append('kaidou')
    characterss = choice(characters)
    return jsonify(character=characterss)