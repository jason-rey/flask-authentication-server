from flask import request
from flask_restful import Resource

from resources.verify_request import VerifyRequest
from db_utils.database_interface import Database
from security_utils import Encryption


class RegisterUser(Resource):
    def __init__(self, _db: Database):
        self.db = _db
        self.requiredBodyFields = ["username", "password"]

    def post(self):
        isValidRequest = VerifyRequest.is_valid_request(
            request, 
            expectedContentType="application/json",
            requiredBodyFields=self.requiredBodyFields
        )
        if not isValidRequest:
            return "incorrect parameters", 400
        
        body = request.json
        salt = Encryption.generate_salt(32)
        passHash = Encryption.hash_with_salt(body["password"], salt)

        self.db.insert_user_data(body["username"], passHash, salt)
        