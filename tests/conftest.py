import os
import pytest
from project import create_app, database
from flask import current_app
from project.models import Stock, User 

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

@pytest.fixture(scope='module')
def new_user():
	user = User('patrick@email.com', 'FlaskIsAwesome123')
	return user

@pytest.fixture(scope='module')
def register_default_user(test_client):
     test_client.post('/users/register',
                      data={'email': 'patrick@gmail.com',
                            'password': 'FlaskIsAwesome123'},
                      follow_redirects=True)
     return 

@pytest.fixture(scope='function')
def log_in_default_user(test_client, register_default_user):
    test_client.post('/users/login',
                    data={'email': 'patrick@gmail.com',
                           'password': 'FlaskIsAwesome123'},
                    follow_redirects=True)
    
    yield

    test_client.get('/users/logout', follow_redirects=True)