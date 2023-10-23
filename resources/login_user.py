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
        self.requiredHeaders = ["ip", "port"]
        self.requiredBodyFields = ["username", "password"]

    def post(self):
        isValidRequest = VerifyRequest.is_valid_request(
            request, 
            expectedContentType="application/json",
            requiredHeaders=self.requiredHeaders,
            requiredBodyFields=self.requiredBodyFields
        )
        if not isValidRequest:
            return "incorrect parameters", 400

        username = request.json["username"]
        password = request.json["password"]
        
        if not self.db.does_username_exist(username):
            return "incorrect username and/or password", 401
        
        userData = self.db.get_user_data(username)
        givenHash = Encryption.hash_with_salt(password, userData["salt"])

        if givenHash != userData["hash"]:
            return "incorrect username and/or password", 401

        tokenHoursToLive = 1
        expiryTimeStamp = datetime.now() + timedelta(hours=tokenHoursToLive)
        format = "%Y-%m-%d %H:%M:%S" 
        ip = request.headers["ip"]
        port = request.headers["port"]
        data = {
            "username": username,
            "ip": ip,
            "port": port,
            "expiryTime": expiryTimeStamp.strftime(format)
        }

        token = jwt.encode(
            payload=data,
            key=Config.JWT_SECRET
        )

        return token