import jwt
from settings import Config

class AuthService():

    @classmethod
    def generate_jwt(cls, payload):
        generated_jwt = jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")
        return generated_jwt
    
    @classmethod
    def check_jwt(cls, jwt_code):
        coded_data = jwt.decode(jwt_code, Config.SECRET_KEY, algorithms="HS256")
        print(coded_data)
        return coded_data