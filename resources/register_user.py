from flask import request
from flask_restful import Resource
from flask import Response

from resources.verify_request import VerifyRequest
from db_utils.database_interface import Database
from security_utils import Encryption
from config import Config

class RegisterUser(Resource):
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
        return 200, self.optionsHeaders

    def post(self):
        isValidRequest = VerifyRequest.is_valid_request(
            request, 
            expectedContentType="application/json",
            requiredBodyFields=self.requiredBodyFields
        )
        if not isValidRequest:
            return {"message": "incorrect parameters"}, 400, self.responseHeaders
        
        body = request.json
        salt = Encryption.generate_salt(32)
        passHash = Encryption.hash_with_salt(body["password"], salt)

        if self.db.does_username_exist(body["username"]):
            return {"message": "username exists"}, 409, self.responseHeaders

        self.db.insert_user_data(body["username"], passHash, salt)
        return None, 201, self.responseHeaders
        
        
        