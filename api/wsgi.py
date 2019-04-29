from flask import Flask

app = Flask(__name__)
app.secret_key = b'yhb77sw9_"F4Q8z\n\xec]/'

from .views import *
