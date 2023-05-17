#! usr/bin/python3

from getpass import getpass
import hashlib
from typing import Any
import uuid

account_dict = {}

class Accounts():

    def __init__(self, username: str, __password: str, phone_number: str | None, id: uuid) -> None:
        if self.is_valid_username(username):
            self.username = username
        
        if self.is_valid_password(__password):
            __password = hashlib.md5(str.encode(__password)).hexdigest()
            self.__password = __password
        
        self.phone_number = phone_number
        self.id = id


    def is_valid_username(self, username):
        if username in account_dict:
            raise ValueError("username already exists")
        return True
    

    def is_valid_password(self, password):
        if len(password) < 4:
            raise ValueError("Password is too short.")
        return True
    
    
    @classmethod
    def new_account(cls, username):
        account_dict[f"{username}"] = cls

    
    def change_phone_user(self, new_user, new_phone):
        
        if new_phone == "":
            new_phone = self.phone_number
        
        if new_user == "":
            new_user = self.username
        
        
        x = Accounts(new_user, self.__password, new_phone, self.id)
        x.new_account(new_user) 


    def check_login(username, password):
        password = hashlib.md5(str.encode(password)).hexdigest()
        if username in account_dict:
            test_object = account_dict[f"{username}"]
        
        if test_object.__password == password:
            return True 
        raise ValueError("No account Found!")

    
    def __str__(self):
        return f"username: {self.username}, phone number: {self.phone_number}, id: {self.id}"
    



