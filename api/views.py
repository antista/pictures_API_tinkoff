import json

from flask import request, url_for


from .models import add_picture,get_picture,q
from .wsgi import app

from rq import Connection, Worker


@app.route('/api/pictures/', methods=['POST'])
def handle_users_request():
    if request.method == 'POST':
        picture_id = add_picture('1234')
        if not picture_id:
            return json.dumps({}), 406
        return json.dumps({'url': url_for('handle_user_request',picture_id=picture_id)}), 200
    return 405


@app.route('/api/pictures/<picture_id>', methods=['GET'])
def handle_user_request(picture_id):
    if request.method == 'GET':
        picture_code = get_picture(picture_id)
        if not picture_code:
            return json.dumps({}), 204
        print(picture_code)
        return json.dumps({'picture': picture_code.decode()}), 200
    return 405


