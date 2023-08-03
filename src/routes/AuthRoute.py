from email_validator import validate_email, EmailNotValidError
from flask import Blueprint, jsonify, request, make_response
from datetime import datetime, timedelta
from src.auth import AuthService

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["POST"])
def log_in_user():
    from src.models.UserModel import User

    try:
        request_body = request.json
        expiration_time = datetime.now() + timedelta(hours=8)
        user_email, user_password = request_body["email"], request_body["password"]
        id_verified_user = User.verify_password(user_email, user_password)
        if not id_verified_user:
            return make_response(jsonify({"message": "Invalid Credentials."}, 401))
        
        generated_jwt = AuthService.generate_jwt({"id_user": id_verified_user, "user_email": user_email ,"user_password": user_password, "expiration_time": str(expiration_time.timestamp())})
        return make_response(jsonify({"token": generated_jwt}), 200)
    except Exception:
        return make_response(jsonify({"error": "Check request body"}), 400)

@auth.route('/register', methods=["POST"])
def register_user():
    from src.models.UserModel import User

    try:
        request_body = request.json
        user_name, user_email, user_password = request_body["username"], request_body["email"], request_body["password"]

        if len(user_name) < 5:
            raise ValueError('Username needs to be longer than 5 characters.')
        
        validate_email(user_email, check_deliverability=True)

        if len(user_password) < 7:
            raise ValueError('Passwords needs to be longer than 7 characters.')

        created_user = User.create_user(user_name,user_email,user_password)
        return make_response(jsonify({"registered": created_user}), 201)
    except Exception as ex:
        return make_response(jsonify({"error": ex.args[0]}), 400)
    
@auth.route('/refresh-token', methods=["POST"])
def refresh_user_token():
    from src.models.UserModel import User

    try:
        token = request.headers["token"]
        jwted_payload = AuthService.check_jwt(jwt_code=token)
        jwted_user_id = jwted_payload["id_user"]
        expiration_time = datetime.now() + timedelta(hours=8)
        verified_user_id = User.verify_password(jwted_payload["user_email"], jwted_payload["user_password"])
        if not (jwted_user_id == verified_user_id):
            return make_response(jsonify({"message": "Invalid Auth Token"}), 401)
        
        refreshed_token = AuthService.generate_jwt({"id_user": jwted_user_id, "user_email": jwted_payload["user_email"] ,"user_password": jwted_payload["user_password"], "expiration_time": str(expiration_time.timestamp())})
        return make_response(jsonify({"new_token": refreshed_token}))
    except Exception:
        return make_response(jsonify({"message": "Invalid Auth Token"}), 400)