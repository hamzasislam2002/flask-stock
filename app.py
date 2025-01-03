# from flask import Flask, render_template, request, session, redirect, url_for, flash
# from markupsafe import escape
# from pydantic import BaseModel, field_validator, ValidationError
# import logging
# from flask.logging import default_handler
# from logging.handlers import RotatingFileHandler

import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask.logging import default_handler
import os
from project import create_app

# class StockModel(BaseModel):
#     stock_symbol: str
#     number_of_shares: int
#     purchase_price: float

#     @field_validator('stock_symbol')
#     def stock_symbol_check(cls, value):
#         if not value.isalpha() or len(value) > 5:
#             raise ValueError('Stock symbol must be 1-5 characters')
#         return value.upper()

app = create_app()
# config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
# app.config.from_object(config_type)
# app.config.from_object('config.DevelopmentConfig')


# app.logger.removeHandler(default_handler)

# app.config.from_pyfile(os.environ['YOUR_APPLICATION_SETTINGS'])

# app.config.from_envvar('YOUR_APPLICATION_SETTINGS')

# app.secret_key = 'BAD_SECRET_KEY'

# from project.stocks import stocks_blueprint
# from project.users import users_blueprint

# app.register_blueprint(stocks_blueprint)
# app.register_blueprint(users_blueprint, url_prefix='/users')

# app.secret_key = 'BAD_SECRET_KEY'

# app.logger.removeHandler(default_handler)

# file_handler = RotatingFileHandler('instance/flask-stock-portfolio.log',
#                                    maxBytes=16384,
#                                    backupCount=20)
# file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
# file_handler.setFormatter(file_formatter)
# file_handler.setLevel(logging.INFO)
# app.logger.addHandler(file_handler)

# from project.stocks import stocks_blueprint
# from project.users import users_blueprint

# app.register_blueprint(stocks_blueprint)
# app.register_blueprint(users_blueprint, url_prefix='/users')

# file_Handler = logging.FileHandler('flask-stock-portfolio.log')
# app.logger.addHandler(file_Handler)

# app.logger.info('Starting the Flask Stock Portfolio App...')

# # @app.route('/')
# # def index():
# #     return 'Hello World'

# @app.route('/')
# def index():
#     app.logger.info('Calling the index() function.')
#     return render_template('index.html')

# @app.route('/about')
# def about():
#     flash('Thanks for learning about this site!', 'info')
#     return render_template('about.html', company_name = "TestDriven.io")

# @app.route('/stocks/')
# def stocks():
#     return render_template('stocks.html')

# @app.route('/hello/<message>')
# def hello_message(message):
#     return f"<h1>Welcome {escape(message)}!</h1>"

# # @app.route('/blog_posts/<post_id>')
# # def display_blog_post(post_id):
# #     return f"<h1>Blog Post #{post_id}...</h1>"

# @app.route('/blog_posts/<int:post_id>')
# def display_blog_post(post_id):
#     return f"<h1>Blog Post #{post_id}...</h1>"

# @app.route('/add_stock', methods=['GET', 'POST'])
# def add_stock():
#     if request.method == 'POST':
#         for k, v in request.form.items():
#             print(f'{k}: {v}')

#         try:
#             stock_data = StockModel(
#                 stock_symbol = request.form['stock_symbol'],
#                 number_of_shares = request.form['number_of_shares'],
#                 purchase_price = request.form['purchase_price']
#             )
#             print(stock_data)

#             session['stock_symbol'] = stock_data.stock_symbol
#             session['number_of_shares'] = stock_data.number_of_shares
#             session['purchase_price'] = stock_data.purchase_price
#             flash(f"Added new stock ({stock_data.stock_symbol})!", 'success')
#             app.logger.info(f"Added new stock ({request.form['stock_symbol']})!")

#             return redirect(url_for('stocks'))
#         except ValidationError as e:
#             print(e)

#     return render_template('add_stock.html')