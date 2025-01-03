from project.models import Stock

def test_new_stock(new_stock):
    # stock = Stock('AAPL', '16', '406.78')
    assert new_stock.stock_symbol == 'AAPL'
    assert new_stock.number_of_shares == 16
    assert new_stock.purchase_price == 40678

