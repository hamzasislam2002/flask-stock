def test_get_registration_page(test_client):
    response = test_client.get('/users/register')
    assert response.status_code == 200
    assert b'Flask Stock Portfolio App' in response.data
    assert b'User Registration' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data

def test_valid_registration(test_client):
    response = test_client.post('/users/register',
                                data={'email': 'patrick@email.com',
                                      'password': 'FlaskIsAwesome123'},
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for registering, patrick@email.com!' in response.data
    assert b'Flask Stock Portfolio App' in response.data

def test_invalid_registration(test_client):
    response = test_client.post('/users/register',
                                data={'email': 'patrick2@email.com',
                                      'password': ''}, # Empty field is not allowed!
                                      follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for registering, patrick2@email.com!' not in response.data
    assert b'Flask Stock Portfolio App' in response.data
    assert b'[This field is required.]' in response.data

def test_duplicate_registration(test_client):
    test_client.post('/users/register',
                     data = {'email': 'patrick@hotmail.com',
                             'password': 'FlaskIsStillGreat!'},
                      follow_redirects=True)
    response = test_client.post('/users/register',
                                data={'email': 'patrick@hotmail.com',
                                      'password': 'FlaskIsStillGreat!'},
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for registering, patrick@hotmail.com!' not in response.data
    assert b'Flask Stock Portfolio App' in response.data
    assert b'ERROR! Email (patrick@hotmail.com) already exists.' in response.data

def test_get_login_page(test_client):
    response = test_client.get('/users/login')
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Login' in response.data

def test_valid_login_and_logout(test_client, register_default_user):
    response = test_client.post('/users/login',
                                data={'email': 'patrick@gmail.com',
                                      'password': 'FlaskIsAwesome123'},
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for logging in, patrick@gmail.com!' in response.data
    assert b'Flask Stock Portfolio App' in response.data
    assert b'Please log in to access this page.' not in response.data

    response = test_client.get('/users/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Goodbye!' in response.data
    assert b'Flask Stock Portfolio App' in response.data
    assert b'Please log in to access this page.' not in response.data

def test_invalid_login(test_client, register_default_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/users/login' page is posted to (POST) with invalid credentials (incorrect password)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/users/login',
                                data={'email': 'patrick@gmail.com',
                                      'password': 'FlaskIsNotAwesome'},  # Incorrect!
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'ERROR! Incorrect login credentials.' in response.data
    assert b'Flask Stock Portfolio App' in response.data

def test_valid_login_when_logged_in_already(test_client, log_in_default_user):
    response = test_client.post('/users/login',
                                data={'email': 'patrick@gmail.com',
                                      'password': 'FlaskIsAwesome123'},
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Already logged in!' in response.data
    assert b'Flask Stock Portfolio App' in response.data

def test_invalid_logout(test_client):
    response = test_client.post('/users/logout', follow_redirects=True)
    assert response.status_code == 405
    assert b'Goodbye!' not in response.data
    assert b'Flask Stock Portfolio App' in response.data
    assert b'Method Not Allowed' in response.data

def test_invalid_logout_not_logged_in(test_client):
    test_client.get('/users/logout', follow_redirects=True)  # Double-check that there are no logged in users!
    response = test_client.get('/users/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Goodbye!' not in response.data
    assert b'Flask Stock Portfolio App' in response.data
    assert b'Login' in response.data
    assert b'Please log in to access this page.' in response.data