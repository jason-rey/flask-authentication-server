from flask import request
from flask_restful import Resource
import jwt

from db_utils.database_interface import Database
from security_utils import Encryption
from config import Config

class LoginUser(Resource):
    def __init__(self, _db: Database):
        self.db = _db

    def post(self):
        args = request.args
        if len(args) != 2 or "username" not in args or "password" not in args:
            return "incorrect parameters", 400
        
        if not self.db.does_username_exist(args["username"]):
            return "incorrect username and/or password", 401
        
        userData = self.db.get_user_data(args["username"])
        givenHash = Encryption.hash_with_salt(args["password"], userData["salt"]).hex()

        if givenHash != userData["hash"]:
            return "incorrect username and/or password", 401

        data = {
            "username": args["username"]
        }

        token = jwt.encode(
            payload=data,
            key=Config.JWT_SECRET
        )

        return token