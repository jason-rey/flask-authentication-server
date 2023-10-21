from flask_restful import Resource

from db_utils.database_interface import Database

class GetUsers(Resource):
    def __init__(self, _db: Database):
        self.db = _db

    def get(self):
        result = self.db.get_all_users()
        out = {}
        for userData in result:
            username = userData[0]
            hash = userData[1]
            salt = userData[2]
            out[username] = {"hash": hash, "salt": salt}

        return out