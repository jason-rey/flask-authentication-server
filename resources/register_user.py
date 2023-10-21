from flask import request
from flask_restful import Resource

from db_utils.database_interface import Database
from security_utils import Encryption


class RegisterUser(Resource):
    def __init__(self, _db: Database):
        self.db = _db
    
    def post(self):
        args = request.args
        if len(args) != 2 or "username" not in args or "password" not in args:
            return "incorrect parameters", 400
        
        salt = Encryption.generate_salt(32)
        passHash = Encryption.hash_with_salt(args["password"], salt)

        self.db.insert_user_data(args["username"], passHash, salt)
        