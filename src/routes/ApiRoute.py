from flask import Blueprint
from .DiariesRoute import diaries

main = Blueprint('api', __name__)
main.register_blueprint(diaries, url_prefix='/diaries')