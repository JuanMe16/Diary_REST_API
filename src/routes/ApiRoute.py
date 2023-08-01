from flask import Blueprint
from .DiariesRoute import diaries
from .AuthRoute import auth

main = Blueprint('api', __name__)
main.register_blueprint(auth, url_prefix='/auth')
main.register_blueprint(diaries, url_prefix='/diaries')