from flask import request, jsonify, make_response
from datetime import datetime
from functools import wraps
from . import AuthService

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        from src.models import User

        try:
            token = request.headers["token"]
            jwted_payload = AuthService.check_jwt(jwt_code=token)
            jwted_user_id = jwted_payload["id_user"]
            jwt_exp_time = jwted_payload["expiration_time"]
            verified_user_id = User.verify_password(jwted_payload["user_email"], jwted_payload["user_password"])
            if not (jwted_user_id == verified_user_id) or float(jwt_exp_time) <= datetime.now().timestamp():
                return make_response(jsonify({"message": "Invalid Auth Token"}), 401)
        except Exception:
            return make_response(jsonify({"message": "Invalid Auth Token"}), 400)
        
        return f(jwted_user_id, *args, **kwargs)
    return decorator

