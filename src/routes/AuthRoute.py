from flask import Blueprint, jsonify, request, make_response
from src.auth import AuthService

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["POST"])
def log_in_user():
    from src.models.UserModel import User

    try:
        request_body = request.json
        user_email, user_password = request_body["email"], request_body["password"]
        id_verified_user = User.verify_password(user_email, user_password)
        if not id_verified_user:
            return make_response(jsonify({"message": "Invalid Credentials."}, 401))
        
        generated_jwt = AuthService.generate_jwt({"id_user": id_verified_user, "user_email": user_email ,"user_password": user_password})
        return make_response(jsonify({"token": generated_jwt}), 200)
    except Exception:
        return make_response(jsonify({"error": "Check request body"}), 400)

@auth.route('/register', methods=["POST"])
def register_user():
    from src.models.UserModel import User

    try:
        request_body = request.json
        user_name, user_email, user_password = request_body["username"], request_body["email"], request_body["password"]
        created_user = User.create_user(user_name,user_email,user_password)
        return make_response(jsonify({"registered": created_user}), 200)
    except Exception:
        return make_response(jsonify({"error": "Check request body"}), 400)