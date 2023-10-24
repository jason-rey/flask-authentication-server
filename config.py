from dotenv import load_dotenv
import os

load_dotenv()

class Config():
    DB_USER = os.getenv("db_user")
    DB_PWD = os.getenv("db_pwd")
    DB_HOST = os.getenv("db_host")
    DB_NAME = os.getenv("db_name")

    ALLOWED_ORIGIN = os.getenv("allowed_origin")

    JWT_SECRET = os.getenv("jwt_secret")
    JWT_ALGORITHM = os.getenv("jwt_algorithm")
