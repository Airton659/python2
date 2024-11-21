from datetime import datetime
from sqlalchemy import select
from app import db
from app.models.models import User, Post

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

def create_user(username, password, profile_picture=None, bio=None, remember=False,last_login=None):
    '''Cria um novo registro no banco'''
    new_user = User(
        username = username,
        password = password,
        profile_picture = profile_picture,
        bio = bio,
        remember = remember,
        last_login = last_login if last_login else datetime.now()
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def create_post(body,user):
    '''Cria e registra um novo post no banco'''
    post = Post(body=body, author=user, timestamp=datetime.now())
    db.session.add(post)
    db.session.commit()

def get_timeline(user_id=None):
    query = Post.query
    if user_id:
        query = query.filter_by(user_id = user_id)
    query = query.order_by(Post.timestamp.desc()).limit(5)
    return query.all()
