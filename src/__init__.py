from flask import Flask
from decouple import config
from .database import create_database, create_tables

# Routes
from .routes import main

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config("SQLALCHEMY_TRACK_MODIFICATIONS")

db, bcrypt = create_database(app)
create_tables(app, db)

def init_app(config):
    #Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(main, url_prefix='/api/v1')

    return app