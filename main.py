#! usr/bin/python3

import users

def main():
    n = None
    while not n:
        i = input("for finishing program enter 0, for signing up enter 1, for account check enter 2: ")
        match i:
            case "0":
                n = 1
            case "1":
                pass
            case "2":
                    pass