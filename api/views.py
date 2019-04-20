import json

from flask import request, url_for

from .models import Pictures
from .wsgi import app


@app.route('/api/pictures/', methods=['POST'])
def handle_add_picture_request():
    if request.method == 'POST':
        picture_id = Pictures.add_picture(request.json)
        if not picture_id:
            return json.dumps({}), 406
        return json.dumps({'url': url_for('handle_get_picture_request', picture_id=picture_id)}), 200
    return 405


@app.route('/api/pictures/<picture_id>', methods=['GET'])
def handle_get_picture_request(picture_id):
    if request.method == 'GET':
        picture_code = Pictures.get_picture(picture_id)
        if not picture_code:
            return json.dumps({}), 204
        return json.dumps({'picture': picture_code.decode()}), 200
    return 405
