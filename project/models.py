from project import database
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
import flask_login

class Stock(database.Model):

    __tablename__ = 'stocks'

    id = mapped_column(Integer(), primary_key=True)
    stock_symbol = mapped_column(String())
    number_of_shares = mapped_column(Integer())
    purchase_price = mapped_column(Integer())

    def __init__(self, stock_symbol: str, number_of_shares: str, purchase_price: str):
        self.stock_symbol = stock_symbol
        self.number_of_shares = int(number_of_shares)
        self.purchase_price = int(float(purchase_price) * 100)

    def __repr__(self):
        return f'{self.stock_symbol} - {self.number_of_shares} shares purchased at ${self.purchase_price / 100}'
    
class User(flask_login.UserMixin, database.Model):

    __tablename__ = 'users'

    id = mapped_column(Integer(), primary_key = True)
    email = mapped_column(String(), unique=True)
    password_hashed = mapped_column(String(128))

    def __init__(self, email: str, password_plaintext: str):
        self.email = email
        self.password_hashed = self._generate_password_hash(password_plaintext)

    def is_password_correct(self, password_plaintext: str):
        return check_password_hash(self.password_hashed, password_plaintext)
    
    @staticmethod
    def _generate_password_hash(password_plaintext):
        return generate_password_hash(password_plaintext)
    
    def __repr__(self):
        return f'<User: {self.email}>'