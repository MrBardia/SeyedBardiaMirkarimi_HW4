#! usr/bin/python3

from getpass import getpass
import hashlib
from typing import Any
from uuid import uuid4



class Accounts():

    account_dict = {}    

    def __init__(self, username: str, __password: str, phone_number=None) -> None:
        self.username = username
        self.__password = __password        
        self.phone_number = phone_number
        self.id = uuid4()

    
    @staticmethod
    def is_valid_username(username, dictionary: dict):
        if username in dictionary:
            raise ValueError("username already exists")
        return True
    
    
    @staticmethod
    def is_valid_password(password):
        if len(password) < 4:
            raise ValueError("Password is too short.")
        return True
    
    
    @classmethod
    def new_account(cls, username):
        cls.account_dict[f"{username}"] = cls

    
    def update_password(self):
        pass

    
    def update_profile(self, new_user, new_phone):
        
        if new_phone == "":
            new_phone = self.phone_number
        
        if new_user == "":
            new_user = self.username
        
        
        x = Accounts(new_user, self.__password, new_phone, self.id)
        x.new_account(new_user) 


    def login(self, username, password):
        password = hashlib.md5(str.encode(password)).hexdigest()
        if username in self.account_dict:
            test_object = self.account_dict[f"{username}"]
        
        if test_object.__password == password:
            return True 
        raise ValueError("No account Found!")

    
    def __str__(self):
        return f"username: {self.username}, phone number: {self.phone_number}, id: {self.id}"
    



