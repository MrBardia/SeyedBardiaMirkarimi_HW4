#! usr/bin/python3


import hashlib
from uuid import uuid4


class Accounts:
    account_dict = {}

    def __init__(self, username: str, __password: str, phone_number=None) -> None:
        self.username = username
        self.__password = __password
        self.phone_number = phone_number
        self.id = uuid4()

    @staticmethod
    def build_pass(password):
        pass_hash = hashlib.sha256(str.encode(password)).hexdigest()
        return pass_hash

    @staticmethod
    def is_valid_username(username, dictionary: dict):
        if username in dictionary:
            raise ValueError("username already exists")
        else:
            return True

    @staticmethod
    def is_valid_password(password):
        if len(password) < 4:
            raise ValueError("Password is too short.")
        else:
            return True

    @classmethod
    def new_account(cls, username: str, __password: str, phone_number=None):
        if cls.is_valid_username(username, cls.account_dict):
            if cls.is_valid_password(__password):
                password = cls.build_pass(__password)
                user1 = cls(username, password, phone_number)
                cls.account_dict[username] = user1
                return user1
            else:
                raise ValueError("Password is too short.")
        else:
            raise ValueError("username already exist.")

    def update_password(self):
        pass

    def update_profile(self, new_user, new_phone):
        pass

    @classmethod
    def login(cls, username, password):
        pass
        if username in cls.account_dict:
            user_test = cls.account_dict[username]
            user_pass = user_test.__repr__()
            if user_pass == cls.build_pass(password):
                return True
            else:
                raise ValueError("Invalid Password!")
        else:
            raise ValueError("Invalid username!")

    def get_password(self):
        return self.__password

    def __str__(self):
        return f"username: {self.username}, phone number: {self.phone_number}, id: {self.id}"

    def __repr__(self):
        return self.__password


user = Accounts.new_account("bardia", "1234")
Accounts.login("bardia", "1234")
