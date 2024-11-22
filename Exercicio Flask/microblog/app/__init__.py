import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
login= LoginManager(app)

app.config['SECRET_KEY']= 'Bk4$!8B9~{*>'
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite+pysqlite:///microblog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()


db.init_app(app)


from app import routes,alquimias
from app.models import models

with app.app_context():
    db.create_all()