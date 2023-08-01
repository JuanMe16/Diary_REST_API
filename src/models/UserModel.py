from sqlalchemy.dialects.mysql import VARCHAR
from src.database import db, bcrypt
from sqlalchemy import select
import sqlalchemy as sa

class User(db.Model):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, unique=True, nullable=False)
    name = sa.Column(sa.String(25), nullable=False)
    email = sa.Column(sa.String(60), unique=True, nullable=False)
    password = sa.Column(sa.String(72), nullable=False)

    @classmethod
    def create_user(cls, user_name, user_email, user_password):
        new_user = cls(name=user_name, email=user_email,
                       password=bcrypt.generate_password_hash(user_password))
        db.session.add(new_user)
        db.session.commit()
        return True
    
    @classmethod
    def verify_password(cls, email, password):
        check_user = db.session.execute(select(User).filter_by(email=email)).scalar_one()
        if not check_user or not bcrypt.check_password_hash(check_user.password, password):
            return False
        return check_user.id