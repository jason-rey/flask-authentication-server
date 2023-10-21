import os
from dotenv import load_dotenv
import mysql.connector

def setup():
    DB_NAME = "LoginData"
    load_dotenv()
    db = mysql.connector.connect(
        host=os.getenv("db_host"),
        user=os.getenv("db_user"),
        password=os.getenv("db_pwd")
    )
    cursor = db.cursor()
    cursor.execute(f"CREATE DATABASE {DB_NAME}")

    db = mysql.connector.connect(
        host=os.getenv("db_host"),
        user=os.getenv("db_user"),
        password=os.getenv("db_pwd"),
        database=DB_NAME
    )
    cursor = db.cursor()
    cursor.execute("CREATE TABLE user_data (username VARCHAR(30), hash VARCHAR(64), salt VARCHAR(64))")
    
if __name__ == "__main__":
    db = mysql.connector.connect(
        host=os.getenv("db_host"),
        user=os.getenv("db_user"),
        password=os.getenv("db_pwd"),
        database="LoginData"
    )
    cursor = db.cursor()
    # setup()

