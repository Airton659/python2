from datetime import datetime
from sqlalchemy import select
from app import db
from app.models.models import User

def validate_user_password(username, password):
    # '''Testa se o usuário e senha correspondem a um registro no banco'''
    res = db.session.scalars(select(User).where(User.username == username))
    user = res.first()
    if user and user.password == password: return user
    else: return None

def user_exist(username):
    '''Testa se o usuário informado corresponde a um registro no banco'''
    res = db.session.scalars(select(User).where(User.username == username))
    user = res.first()
    return user

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
    return new_user
