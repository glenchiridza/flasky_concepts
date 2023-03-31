from flask import Flask

from flask_bcrypt import Bcrypt

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
app.config['SECRET_KEY'] = 'e7ca173068401e2f66dd47f0'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes