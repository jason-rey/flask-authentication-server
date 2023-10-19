from db_utils.database_interface import Database
from flask_restful import Resource


class RegisterUser(Resource):
    def __init__(self, _db: Database):
        self.db = _db
    
    def post(self):
        pass