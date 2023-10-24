from flask_restful import Resource
from flask import Response
import json

from db_utils.database_interface import Database
from config import Config

class GetUsers(Resource):
    def __init__(self, _db: Database):
        self.db = _db
        self.responseHeaders = {"Access-Control-Allow-Origin": Config.ALLOWED_ORIGIN}
        self.options = {
            "Access-Control-Allow-Origin": Config.ALLOWED_ORIGIN,
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "POST"
        }
    
    def get(self):
        result = self.db.get_all_users()
        out = {}
        for userData in result:
            username = userData[0]
            hash = userData[1]
            salt = userData[2]
            out[username] = {"hash": hash, "salt": salt}

        return out, 200, self.responseHeaders