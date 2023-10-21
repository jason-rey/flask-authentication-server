import mysql.connector

from db_utils.database_interface import Database
from config import Config

class SQL(Database):
    def __init__(self):
        self.db = mysql.connector.connect(
            host = "localhost",
            user = Config.DB_USER,
            password = Config.DB_PWD,
            database = Config.DB_NAME
        )
        self.cursor = self.db.cursor()
    
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