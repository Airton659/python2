import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'Bk4$!8B9~{*>'

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite+pysqlite:///microblog.db"
db = SQLAlchemy()
db.init_app(app)


from app import routes,alquimias
from app.models import models

with app.app_context():
    db.create_all()