import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(db_dir, "site.db")}'
db = SQLAlchemy(app)

from flaskblog import routes