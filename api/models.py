import time

import redis
from rq import Queue
from uuid import uuid4

r = redis.Redis(host='localhost', port=6379, db=0)
q = Queue('high', connection=r)
q.empty()


def add_picture(picture_code):
    picture_id = uuid4().hex
    # r.set('picture:%s:code' % picture_id, picture_code)
    q.enqueue(add_to_db, picture_id, picture_code)
    return picture_id


def add_to_db(picture_id, picture_code):
    print('====================')
    r.set('picture:%s:code' % picture_id, picture_code)
    print('------------------')


def get_from_db(picture_id):
    # return r.get('picture:%s:code' % picture_id)
    return '123457'


def get_picture(picture_id):
    # picture_code = q.enqueue(get_from_db, picture_id)
    # print(picture_code)
    # print(picture_code.result)
    # time.sleep(5)
    # print(picture_code)
    # print(picture_code.result)
    return r.get('picture:%s:code' % picture_id)
    # return picture_code.result
