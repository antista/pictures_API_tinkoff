import json


from api.wsgi import app


def test_handle_pictures_request_post(mocker, test_client):
    mocker.patch('api.models.Pictures.add_picture', return_value='1234')
    with app.test_request_context():
        response = test_client.post('/api/pictures/')
        assert response.status_code == 200
        assert response.data == b'{"url": "/api/pictures/1234"}'


def test_handle_pictures_request_post_wrong(mocker, test_client):
    mocker.patch('api.models.Pictures.add_picture', return_value=None)
    with app.test_request_context():
        response = test_client.post('/api/pictures/')
        assert response.status_code == 406
        assert response.data.decode() == '{}'


def test_handle_pictures_request_get_not_existed(mocker, test_client):
    mocker.patch('api.models.Pictures.add_picture', return_value=json.dumps({}))
    with app.test_request_context():
        response = test_client.get('/api/pictures/1234')
        assert response.status_code == 204
        assert response.data.decode() == ''


def test_handle_pictures_request_unknown_command(test_client):
    with app.test_request_context():
        response = test_client.put('/api/pictures/')
        assert response.status_code == 405
#
#
# def test_handle_user_request_get(mocker, test_client):
# mocker.patch('api.models.User.get_user', return_value=None)
# with app.test_request_context():
# response = test_client.get('/api/users/123')
# assert response.status_code == 204
# mocker.patch('api.models.User.get_user', return_value=json.dumps({}))
# with app.test_request_context():
# response = test_client.get('/api/users/123')
# assert response.status_code == 200
# assert response.data.decode() == '{}'
