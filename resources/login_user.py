from flask import request
from flask_restful import Resource
import jwt
from datetime import datetime, timedelta

from resources.verify_request import VerifyRequest
from db_utils.database_interface import Database
from security_utils import Encryption
from config import Config

class LoginUser(Resource):
    def __init__(self, _db: Database):
        self.db = _db
        self.requiredBodyFields = ["username", "password"]
        self.responseHeaders = {"Access-Control-Allow-Origin": Config.ALLOWED_ORIGIN}
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
            requiredBodyFields=self.requiredBodyFields
        )
        if not isValidRequest:
            return {"message": "incorrect parameters"}, 400, self.responseHeaders

        username = request.json["username"]
        password = request.json["password"]
        
        if not self.db.does_username_exist(username):
            return {"message": "incorrect username and/or password"}, 401, self.responseHeaders
        
        userData = self.db.get_user_data(username)
        givenHash = Encryption.hash_with_salt(password, userData["salt"])

        if givenHash != userData["hash"]:
            return {"message": "incorrect username and/or password"}, 401, self.responseHeaders

        tokenHoursToLive = 1
        expiryTimeStamp = datetime.now() + timedelta(hours=tokenHoursToLive)
        format = "%Y-%m-%d %H:%M:%S" 
        ip = request.remote_addr
        data = {
            "username": username,
            "ip": ip,
            "expiryTime": expiryTimeStamp.strftime(format)
        }

        token = jwt.encode(
            payload=data,
            key=Config.JWT_SECRET
        )
        
        return {"token": token}, 200, self.responseHeaders