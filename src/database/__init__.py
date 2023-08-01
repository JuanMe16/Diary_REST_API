from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db: SQLAlchemy
bcrypt: Bcrypt

def create_database(app: Flask):
    global db, bcrypt
    db = SQLAlchemy(app)
    bcrypt = Bcrypt(app)
    
    return db, bcrypt

def create_tables(app: Flask, db: SQLAlchemy):
    from src.models import Diary, User

    with app.app_context():
        db.create_all()