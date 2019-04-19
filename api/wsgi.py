# from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from .models import q

from rq import Connection, Worker

app = Flask(__name__)

# db_conn = 'postgres+psycopg2://admin:12345678@localhost:5432/cinema'

# app.config['SQLALCHEMY_DATABASE_URI'] = db_conn
# db = SQLAlchemy(app)
# app.secret_key = b'yhb77sw9_"F4Q8z\n\xec]/'
# with Connection():
#     w = Worker(q)
#     w.work()
from .views import *
