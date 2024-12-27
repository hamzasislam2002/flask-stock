from app import app

def test_index_page():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Flask Stock Portfolio App' in response.data
        assert b'Welcome to the' in response.data
        assert b'Flask Stock Portfolio App!' in response.data

def test_about_page():
    with app.test_client() as client:
        response = client.get('/about')
        assert response.status_code == 200
        assert b'Flask Stock Portfolio App' in response.data
        assert b'About' in response.data
        assert b'This application is built using the Flask web framework.' in response.data
        assert b'Course developed by TestDriven.io' in response.data

def test_get_add_stock_page():
    with app.test_client() as client:
        response = client.get('/add_stock')
        assert response.status_code == 200
        assert b'Flask Stock Portfolio App' in response.data
        assert b'Add a Stock' in response.data
        assert b'Stock Symbol <em>(required, 1-5 upper case letters)</em>' in response.data
        assert b'Number of Shares <em>(required)</em>' in response.data
        assert b'Purchase Price ($) <em>(required)</em>' in response.data

def test_post_add_stock_page():
    with app.test_client() as client:
        response = client.post('/add_stock',
                               data={'stock_symbol': 'AAPL',
                                     'number_of_shares': '23',
                                     'purchase_price': '432.17'
                                     },
                               follow_redirects=True)
        assert response.status_code == 200
        assert b'List of Stocks' in response.data
        assert b'Stock Symbol' in response.data
        assert b'Number of Shares' in response.data
        assert b'Purchase Price' in response.data
        assert b'AAPL' in response.data
        assert b'23' in response.data
        assert b'432.17' in response.data
