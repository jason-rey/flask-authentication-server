from flask import Flask
from flask_restful import Api

from db_utils import database_interface, MySQLdatabase
import resources
from config import Config

db = MySQLdatabase.MySQL()
db.make_all()
app = Flask(__name__)
api = Api(app)
if not issubclass(type(db), database_interface.Database):
    raise Exception("Database does not implement expected interface")

api.add_resource(resources.RegisterUser, "/register-user", resource_class_args={db})
api.add_resource(resources.LoginUser, "/login-user",  resource_class_args={db})
api.add_resource(resources.GetUsers, "/get-users", resource_class_args={db}) # testing endpoint, dont forget to remove later
api.add_resource(resources.AuthenticateToken, "/authenticate-token")

if __name__ == "__main__":
    app.run(debug=True)
