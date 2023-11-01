class Database():
    def make_all(self):
        raise Exception("interface method make_all not implemented")

    def get_user_data(self, username):
        raise Exception("interface method get_user_data not implemented")

    def does_username_exist(self, username):
        raise Exception("interface method does_username_exist not implemented")

    def insert_user_data(self, username, hash, salt):
        raise Exception("interface method insert_user_data not implemented")

    # test method remove later
    def get_all_users(self):
        pass