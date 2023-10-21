from flask import request
from flask_restful import Resource
import jwt

from config import Config

class AuthenticateToken(Resource):
    def post(self):
        headers = request.headers
        if len(headers) < 2 or "token" not in headers or "username" not in headers:
            return "incorrect headers", 400
        givenUsername = headers.get("username")
        token = headers.get("token")

        try:
            data = jwt.decode(
                token,
                algorithms=[Config.JWT_ALGORITHM],
                key=Config.JWT_SECRET
            )

            if givenUsername != data["username"]:
                return "invalid token", 401

            return 200
        except Exception as e:
            return str(e), 401