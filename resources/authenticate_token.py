from flask import request
from flask_restful import Resource

class AuthenticateToken(Resource):
    def get(self):
        args = request.args
        if "name" in args:
            return f"name is: {args["name"]}"
        else:
            return "query not correct"