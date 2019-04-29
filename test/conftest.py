import pytest
from api.models import r

from api import wsgi


@pytest.fixture
def app():
    return wsgi.app


@pytest.fixture(scope='module')
def test_client():
    flask_app = wsgi.app
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(autouse=True)
def clean_db():
    r.flushdb()
