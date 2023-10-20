from flask import request
from flask_restful import Resource

from db_utils.database_interface import Database

class LoginUser(Resource):
    def post(self):
        args = request.args
        if len(args) != 2 or "username" not in args or "password" not in args:
            return "incorrect parameters", 400