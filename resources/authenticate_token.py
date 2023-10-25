from flask import request
from flask_restful import Resource
import jwt
from datetime import datetime

from resources.verify_request import VerifyRequest
from config import Config

class AuthenticateToken(Resource):
    def __init__(self):
        self.requiredHeaders = ["username"]
        self.requiredBodyFields = ["token"]
        self.responseHeaders = {
            "Access-Control-Allow-Origin": Config.ALLOWED_ORIGIN
        }
        self.optionsHeaders = {
            "Access-Control-Allow-Origin": Config.ALLOWED_ORIGIN,
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "POST"
        }

    def options(self):
        return {}, 200, self.optionsHeaders

    def post(self):
        isValidRequest = VerifyRequest.is_valid_request(
            request, 
            expectedContentType="application/json",
            requiredHeaders=self.requiredHeaders, 
            requiredBodyFields=self.requiredBodyFields
        )
        if not isValidRequest:
            return {"message": "invalid request"}, 400, self.responseHeaders
        
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
                return {"message": "token is expired"}, 401, self.responseHeaders

            userCredentials = {
                "username": request.headers["username"],
                "ip": request.remote_addr,
                "port": request.environ["REMOTE_PORT"]
            }
            for field in data:
                if field == "expiryTime":
                    continue
                elif data[field] != userCredentials[field]:
                    return {"message": "user credentials does not match with token"}, 401, self.responseHeaders

            return {}, 200, self.responseHeaders
        except Exception:
            return {"message": "incorrect token"}, 401, self.responseHeaders