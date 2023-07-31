import sqlalchemy as sa
from src.database import db

class User(db.Model):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, unique=True, nullable=False)
    name = sa.Column(sa.String(25), nullable=False)
    email = sa.Column(sa.String(60), unique=True, nullable=False)
    password = sa.Column(sa.String(40), nullable=False)