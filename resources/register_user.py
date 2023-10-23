from flask import request
from flask_restful import Resource

from resources.verify_request import VerifyRequest
from db_utils.database_interface import Database
from security_utils import Encryption


class RegisterUser(Resource):
    def __init__(self, _db: Database):
        self.db = _db
        self.requiredArgs = ["username", "password"]

    def post(self):
        isValidRequest = VerifyRequest.is_valid_request(request, 
            requiredArgs=self.requiredArgs
        )
        if not isValidRequest:
            return "incorrect parameters", 400
        
        args = request.args
        salt = Encryption.generate_salt(32)
        passHash = Encryption.hash_with_salt(args["password"], salt)

        self.db.insert_user_data(args["username"], passHash, salt)
        