from datetime import datetime
from sqlalchemy import select
from app import db
from app.models.models import User

def validate_user_password(username, password):
    '''Testa se o usuário e senha correspondem a um registro no banco'''
    res = db.session.scalars(select(User).where(User.username == username))
    res = res.first()
    return res and res.password == password

def user_exist(username):
    '''Testa se o usuário informado corresponde a um registro no banco'''
    res = db.session.scalars(select(User).where(User.username == username))
    return res.first()

def create_user(username, password, remember=False,last_login=None):
    '''Cria um novo registro no banco'''
    new_user = User(
        username = username,
        password = password,
        remember = remember,
        last_login = last_login if last_login else datetime.now()
    )
    db.session.add(new_user)
    db.session.commit()