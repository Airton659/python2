from app import app
# from app import db
# from app.models.models import User,Post
# from datetime import datetime


# app.app_context().push()

# user = User(username='maria', password='123', last_login = datetime.now())
# db.session.add(user)
# db.session.commit()

# user = db.session.get(User,1)
# post = Post(body='Olá mundo!', author=user, timestamp=datetime.now())
# db.session.add(post)
# db.session.commit()

# user = db.session.get(User,1)
# for post in user.posts:
#     print(post.id, post.body, post.user_id, post.author.username)