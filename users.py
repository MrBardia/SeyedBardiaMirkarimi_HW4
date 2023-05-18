#! usr/bin/python3


import hashlib
from getpass import getpass
from uuid import uuid4


class Accounts:
    """
    A class to save accounts and have signup and login methods.
    """
    account_dict = {}

    def __init__(self, username: str, __password: str, phone_number=None) -> None:
        self.username = username
        self.__password = __password
        self.phone_number = phone_number
        self.id = uuid4()

    @staticmethod
    def build_pass(password: str):
        """
        change normal string password to sha256 hash password
        :param password: string
        :return: sha256 hash password
        """
        pass_hash = hashlib.sha256(str.encode(password)).hexdigest()
        return pass_hash

    @staticmethod
    def is_valid_username(username: str, dictionary: dict) -> bool:
        """
        check for valid username in class dictionary database.
        :param username: string
        :param dictionary: class object
        :return: Boolean
        """
        if username in dictionary or username.isspace():
            raise ValueError("username already exists")
        else:
            return True

    @staticmethod
    def is_valid_password(password: str) -> bool:
        """
        check for valid password length.
        :param password: string
        :return: Boolean
        """
        if len(password) < 4 or password.isspace():
            raise ValueError("Password is too short.")
        else:
            return True

    @classmethod
    def new_account(cls, username: str, __password: str, phone_number=None):
        """
        check validation of username and password and create a new account and save it in dictionary.
        :param username: string
        :param __password:  (private)
        :param phone_number: string (optional)
        :return: user object
        """
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

    def update_password(self, old_password: str):
        """
        take old password for verification and set new password and save in dictionary.
        :param old_password: string
        :return: new account in dictionary
        """
        old_password_hash = Accounts.build_pass(old_password)
        if old_password_hash == self.__password:
            new_password = getpass('input new Password: ')
            confirm_new_password = getpass('input new password confirmation: ')
            if new_password == confirm_new_password:
                del self.account_dict[self.username]
                self.new_account(self.username, new_password, self.phone_number)
            else:
                raise ValueError("New password not confirmed.")
        else:
            raise ValueError("Invalid password.")

    def update_profile(self, new_user: str, new_phone: str):
        """
        update username or phone number (optional) and if one is left blank it will use the old value.
        :param new_user: string
        :param new_phone: string
        :return: new user object in class dictionary.
        """
        if new_user == "":
            new_user = self.username
        else:
            pass

        if new_phone == "":
            new_phone = self.phone_number
        else:
            pass

        del self.account_dict[self.username]
        self.new_account(new_user, self.__password, new_phone)

    @classmethod
    def login(cls, username: str, password: str) -> bool:
        """
        check for username existence and valid password and return boolean.
        :param username:
        :param password:
        :return:
        """
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

    def __str__(self):
        return f"username: {self.username}, phone number: {self.phone_number}, id: {self.id}"

    def __repr__(self):
        return self.__password


user = Accounts.new_account("bardia", "1234")
Accounts.login("bardia", "1234")
