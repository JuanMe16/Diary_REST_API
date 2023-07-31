from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db: SQLAlchemy
ma: Marshmallow

def create_database(app: Flask):
    global db, ma
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    
    return db, ma

def create_tables(app: Flask, db: SQLAlchemy):
    from src.models import Diary, User

    with app.app_context():
        db.create_all()