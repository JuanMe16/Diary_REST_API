from flask import request, jsonify
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
            verified_user_id = User.verify_password(jwted_payload["user_email"], jwted_payload["user_password"])
            if not (jwted_user_id == verified_user_id):
                return jsonify({"message": "Invalid Auth Token"})
        except Exception as ex:
            print(ex)
            return jsonify({"message": "Invalid Auth Token"})
        
        return f(jwted_user_id, *args, **kwargs)
    return decorator

