import mysql.connector

from . import database_interface
from config import Config

class MySQL(database_interface.Database):
    def connect(self):
        db = mysql.connector.connect(
            host = Config.DB_HOST,
            user = Config.DB_USER,
            password = Config.DB_PWD,
            database = Config.DB_NAME
        )

        return db, db.cursor()

    def make_all(self):
        db = mysql.connector.connect(
            host = Config.DB_HOST,
            user = Config.DB_USER,
            password = Config.DB_PWD,
        )
        cursor = db.cursor()
        try:
            cursor.execute(f"CREATE DATABASE {Config.DB_NAME}")
        except:
            print("Database already exists")
        
        try:
            cursor.execute("CREATE TABLE user_data (username VARCHAR(30), hash VARCHAR(64), salt VARCHAR(64))")
        except:
            print("Tables already exist")

        print("Finished making")
        db.database = Config.DB_NAME
        db.commit()
        cursor.close()
        db.close()

    def get_user_data(self, username):
        db, cursor = self.connect()
        cursor.execute(f'SELECT * FROM user_data WHERE username = "{username}"')
        result = cursor.fetchall()[0]
        out = {
            "username": result[0],
            "hash": result[1],
            "salt": result[2]
        }

        cursor.close()
        db.close()
        return out
    
    def does_username_exist(self, username):
        db, cursor = self.connect()
        cursor.execute(f'SELECT * FROM user_data WHERE username = "{username}"')
        result = (len(cursor.fetchall()) > 0)

        cursor.close()
        db.close()
        return result
    
    def insert_user_data(self, username, hash, salt):
        db, cursor = self.connect()
        cursor.execute(
            f'INSERT INTO user_data (username, hash, salt) VALUES("{username}", "{hash}", "{salt}")'
        )
        db.commit()

        cursor.close()
        db.close()

    # used for testing remove this later
    def get_all_users(self):
        db, cursor = self.connect()
        cursor.execute(f"SELECT * FROM user_data")
        result = cursor.fetchall()
        
        cursor.close()
        db.close()
        return result