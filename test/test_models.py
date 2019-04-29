import rq

from api.models import Pictures, r


def test_add_to_db():
    Pictures.add_to_db('4321', 'smth')
    assert r.get('picture:%s:code' % '4321') == b'smth'


def test_get_picture():
    Pictures.add_to_db('4321', 'smth')
    assert Pictures.get_picture('4321') == b'smth'


def test_resize_picture(mocker):
    mocker.patch('rq.Queue.enqueue')
    mocker.patch('PIL.Image.open')
    Pictures.resize_picture('smth', (16, 16), '1234')
    rq.Queue.enqueue.assert_called_once()


def test_add_picture_wrong():
    assert not Pictures.add_picture({})
    assert not Pictures.add_picture({'picture': 'smth', 'size': 'smthwrong'})
