#! usr/bin/python3

from users import Accounts
import users
from getpass import getpass
import hashlib
from typing import Any
import uuid


def main():
    def get_password():
        password = None
        while not password:
            password = getpass("Enter Password: ")
            password_confirm = getpass("Confirm Password: ")
            if password != password_confirm:
                print("Password don't match!")
                password = None            
        return password  
    
    while True:
        i = input("for finishing program enter 0, for signing up enter 1, for account check enter 2: ")
        match i:
            case "0":
                break
            case "1":
                  username = input("Enter your username: ")
                  password = get_password()
                  phone_number = input("Enter your phone Number: ")
                  
                  account1 = Accounts(username, password, phone_number)
                  account1.new_account(username) 
                  print(users.Account.account_dict)               
            case "2":
                    pass
             

