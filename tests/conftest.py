import os
import pytest
from project import create_app, database
from flask import current_app
from project.models import Stock

@pytest.fixture(scope='module')
def test_client():
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()
    # flask_app.config.from_object('config.TestingConfig')

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            flask_app.logger.info('Creating database tables in the test_client() fixture...')

            database.create_all()

    # testing_client = flask_app.test_client()

    # ctx = flask_app.app_context()
    # ctx.push()

    # current_app.logger.info('In the test_client() fixture...')

    # ctx.pop()

        yield testing_client 

        with flask_app.app_context():
            database.drop_all()

@pytest.fixture(scope='module')
def new_stock():
    stock = Stock('AAPL', '16', '406.78')
    return stock