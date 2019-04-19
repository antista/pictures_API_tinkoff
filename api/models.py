import base64
import io
from uuid import uuid4
from PIL import Image

from redis import Redis
from rq import Queue

r = Redis(host='localhost', port=6379, db=0)
q = Queue('high', connection=r)


def resize_picture(picture_code, size, picture_id):
    imgdata = base64.b64decode(str(picture_code))
    img = Image.open(io.BytesIO(imgdata))

    img = img.resize(size, Image.ANTIALIAS)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    img = buffer.getvalue()

    picture_code = base64.b64encode(img)
    q.enqueue(add_to_db, picture_id, picture_code)


def add_picture(data):
    if 'picture' not in data.keys() or 'size' not in data.keys():
        return None

    picture_id = uuid4().hex
    picture_code = data['picture']
    try:
        size = tuple(int(x) for x in data['size'].split('x'))
    except ValueError:
        return None

    q.enqueue(add_to_db, uuid4().hex, picture_code)
    q.enqueue(resize_picture, picture_code, size, picture_id)
    return picture_id


def add_to_db(picture_id, picture_code):
    r.set('picture:%s:code' % picture_id, picture_code)


def get_picture(picture_id):
    return r.get('picture:%s:code' % picture_id)
