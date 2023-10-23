import mysql.connector
from config import Config

def setup():
    DB_NAME = Config.DB_NAME
    if DB_NAME == "":
        raise Exception("Empty database name, configure env file first")
    
    db = mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PWD
    )
    cursor = db.cursor()
    cursor.execute(f"CREATE DATABASE {DB_NAME}")

    db = mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PWD,
        database=DB_NAME
    )
    cursor = db.cursor()
    cursor.execute("CREATE TABLE user_data (username VARCHAR(30), hash VARCHAR(64), salt VARCHAR(64))")
    print("Database and table creation successful")

if __name__ == "__main__":
    setup()

