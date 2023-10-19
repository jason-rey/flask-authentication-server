from flask import Flask
from flask_restful import Api, Resource

from db_utils import database_interface, SQLdatabase
import resources

def main():
    app = Flask(__name__)
    api = Api(app)
    db = SQLdatabase.SQL()
    if not issubclass(type(db), database_interface.Database):
        raise Exception("Database does not implement expected interface")
    
    api.add_resource(resources.RegisterUser, "/register-user")
    api.add_resource(resources.LoginUser, "/login-user")
    api.add_resource(resources.AuthenticateToken, "/authenticate-token")
    app.run(debug=True)

if __name__ == "__main__":
    main()
