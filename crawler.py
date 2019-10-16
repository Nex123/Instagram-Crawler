#this is an instagram crawler
from InstagramAPI import InstagramAPI

def get_username() -> str:
    '''Asks user to input Instagram username'''
    while True:
        try:
            name = input("Username: ")
            if name != "":
                return name
            else:
                raise ValueError
        except ValueError:
            print("Username cannot be empty")


def get_password() -> str:
    '''Asks user to input Instagram password'''
    while True:
        try:
            password = input("Password: ")
            if password != "":
                return password
            else:
                raise ValueError
        except ValueError:
            print("Password cannot be empty")

def get_login_info() -> (str, str):
    '''Asks the user to supply both an Instagram username and password'''
    return (get_username(), get_password()) #Maybe add better ways of checking input?


if __name__ == "__main__":
    login_info = get_login_info()
    session = InstagramAPI(username = login_info[0], password = login_info[1])
