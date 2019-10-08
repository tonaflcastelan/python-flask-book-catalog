# auth/models.py
# python code creating a user

from datetime import datetime
from app import db, bcrypt  # app/__init__.py


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now)

    @classmethod
    def create_user(cls, user, email, password):
        user = cls(user_name=user,
                   user_email=email,
                   user_password=bcrypt.generate_password_hash(password).decode('utf-8'))

        db.session.add(user)
        db.session.commit()

        return user
