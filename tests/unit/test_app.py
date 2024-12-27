from app import StockModel
import pytest
from pydantic import ValidationError

def test_validate_stock_data_nominal():
    """
    GIVEN a helper class to validate the form data
    WHEN valid data is passed in
    THEN check that the validation
    """
    stock_data = StockModel(
        stock_symbol = 'SBUX',
        number_of_shares = '100',
        purchase_price = '45.67'
    )
    assert stock_data.stock_symbol == 'SBUX'
    assert stock_data.number_of_shares == 100
    assert stock_data.purchase_price == 45.67

def test_validate_stock_data_invalid_stock_symbol():
    with pytest.raises(ValueError):
        StockModel(
            stock_symbol='SBUX123',
            number_of_shares='100',
            purchase_price='45.67'
        )

def test_validate_stock_data_invalid_number_of_shares():
    with pytest.raises(ValidationError):
        StockModel(
            stock_symbol = 'SBUX',
            number_of_shares='100.1231',
            purchase_price = '45.67'
        )

def test_validate_stock_data_invalid_purchase_price():
    with pytest.raises(ValidationError):
        StockModel(
            stock_symbol = 'SBUX',
            number_of_shares='100',
            purchase_price='45,67'
        )

def test_validate_stock_data_missing_inputs():
    with pytest.raises(ValidationError):
        StockModel()

def test_validate_stock_data_missing_purchase_price():
    with pytest.raises(ValidationError):
        StockModel(
            stock_symbol='SBUX',
            number_of_shares = '100'
        )