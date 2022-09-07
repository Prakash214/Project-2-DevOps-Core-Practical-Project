from application import app
from flask import jsonify
from random import choice

friends = ['zoro', 'sanji', 'jimbei', 'nami', 'luffy', 'usopp', 'chopper', 'robin', 'brook', 'friends']

@app.route('/get-friend', methods=['GET'])
def get_friend():
    friend = choice(friends)
    return jsonify(friend=friend)