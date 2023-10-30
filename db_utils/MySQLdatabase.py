import mysql.connector

from . import database_interface
from config import Config

class MySQL(database_interface.Database):
    def __init__(self):
        self.db = mysql.connector.connect(
            host = Config.DB_HOST,
            user = Config.DB_USER,
            password = Config.DB_PWD,
        )
        self.cursor = self.db.cursor()
    
    def make_all(self):
        try:
            self.cursor.execute(f"CREATE DATABASE {Config.DB_NAME}")
        except:
            print("Database already exists")
        
        try:
            self.cursor.execute("CREATE TABLE user_data (username VARCHAR(30), hash VARCHAR(64), salt VARCHAR(64))")
        except:
            print("Tables already exist")

        print("Finished making")
        self.db.database = Config.DB_NAME
        self.db.commit()

    def get_user_data(self, username):
        self.cursor.execute(f'SELECT * FROM user_data WHERE username = "{username}"')
        result = self.cursor.fetchall()[0]
        out = {
            "username": result[0],
            "hash": result[1],
            "salt": result[2]
        }

        return out
    
    def does_username_exist(self, username):
        self.cursor.execute(f'SELECT * FROM user_data WHERE username = "{username}"')
        result = (len(self.cursor.fetchall()) > 0)
        return result
    
    def insert_user_data(self, username, hash, salt):
        self.cursor.execute(
            f'INSERT INTO user_data (username, hash, salt) VALUES("{username}", "{hash}", "{salt}")'
        )
        self.db.commit()

    # used for testing remove this later
    def get_all_users(self):
        self.cursor.execute(f"SELECT * FROM user_data")
        return self.cursor.fetchall()