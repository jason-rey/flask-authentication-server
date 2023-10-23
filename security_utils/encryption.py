import hashlib
import os

class Encryption():
    @staticmethod
    def generate_salt(length):
        return os.urandom(length).hex()

    @staticmethod
    def hash_with_salt(data, saltHexString):
        salt = bytes.fromhex(saltHexString)
        hash = hashlib.pbkdf2_hmac(
            "sha256",
            data.encode("utf-8"),
            salt,
            100_000
        ).hex()

        return hash

    