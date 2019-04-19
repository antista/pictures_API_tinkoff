import pytest

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
