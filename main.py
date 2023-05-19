#! usr/bin/python3

from users import Accounts
from getpass import getpass


def main():
    def get_password():
        """
        password input function with getpass() method and password confirmation.
        :return: confirmed password value.
        """
        while True:
            new_password = getpass("Enter Password: ")
            password_confirm = getpass("Confirm Password: ")
            if new_password != password_confirm:
                print("Password don't match!")
            break
        return new_password

    while True:
        option = input("Enter your Request Num (0 to exit, 1 to signup, 2 to login): ")
        match option:
            case "0":
                break
            case "1":
                username = input("Enter username: ")
                password = get_password()
                phone_number = input("Enter Phone Number Please (Not necessary): ")
                Accounts.new_account(username, password, phone_number)
            case "2":
                log_in_username = input("Please enter your username: ")
                log_in_password = getpass("Please Enter Your password: ")
                if Accounts.login(log_in_username, log_in_password):
                    logged_user = Accounts.account_dict[log_in_username]
                    while True:
                        log_in_methods = input("Enter 1:info, 2:user and phone edit, 3:password reset, 4:exit : ")
                        match log_in_methods:
                            case "1":
                                print(logged_user)
                            case "2":
                                new_username = input("Enter your new username: ")
                                new_phone_number = input("Enter your new phone number: ")
                                logged_user.update_profile(new_username, new_phone_number)
                            case "3":
                                old_password = getpass("input your old password: ")
                                logged_user.update_password(old_password)
                            case "4":
                                break
                            case _:
                                print("choose a right choice.")
            case _:
                print("choose a right choice.")


if __name__ == "__main__":
    main()
