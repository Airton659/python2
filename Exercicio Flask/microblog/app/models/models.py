from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from app import db
from flask_login import UserMixin
from app import login

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    remember: Mapped[bool] = mapped_column(default=False)
    last_login: Mapped[datetime] = mapped_column()

@login.user_loader
def load_user(id):
    return db.session.get(User,int(id))