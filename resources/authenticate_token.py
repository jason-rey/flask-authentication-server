from flask import request
from flask_restful import Resource
import jwt
from datetime import datetime, timedelta

from resources.verify_request import VerifyRequest
from config import Config

class AuthenticateToken(Resource):
    def __init__(self):
        self.requiredHeaders = ["username", "ip", "port"]
        self.requiredBodyFields = ["token"]

    def post(self):
        isValidRequest = VerifyRequest.is_valid_request(
            request, 
            expectedContentType="application/json",
            requiredHeaders=self.requiredHeaders, 
            requiredBodyFields=self.requiredBodyFields
        )
        if not isValidRequest:
            return "invalid request", 400
        
        token = request.json["token"]

        try:
            data = jwt.decode(
                token,
                algorithms=[Config.JWT_ALGORITHM],
                key=Config.JWT_SECRET
            )

            currTime = datetime.now()
            tokenTime = datetime.strptime(data["expiryTime"], "%Y-%m-%d %H:%M:%S")
            if (tokenTime - currTime).total_seconds() <= 0:
                return "token is expired", 401
            
            for field in data:
                if field == "expiryTime":
                    continue
                elif data[field] != request.headers[field]:
                    return "user credentials does not match with token", 401

            return 200
        except Exception:
            return "invalid token", 401