#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
def create_user(name, password):
    """
    Function to create a new user
    """
    new_user = User(name, password)
    return new_user

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def check_existing_users(name):
    return User.user_exist(name)

def display_users():
    return User.display_users()

def user_log_in(name, password):
    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)
def create_credentials(user_password, name, password):
    new_credentials = Credentials(user_password, name, password)
    return new_credentials

def save_credentials(credentials):
    credentials.save_credentials(credentials)

def check_existing_credentials(name):
    return Credentials.credentials_exist(name)

def display_credentials(password):
    return Credentials.display_credentials(password)

def create_generated_password(name):
    password = Credentials.generate_password()
    return password


def main():
    print("Hello, welcome to your password vault.What would you like to do?")

    print('\n')
    while True:
                    print("Use these short codes : cu - create a new user, du - display users, li - log in, ex -exit the user list and switch to credentials")

                    short_code = input().lower()
                    if short_code == 'cu':
                            print("New User")
                            print("-"*10)

                            print ("user name ....")
                            user_name = input()

                            print("user password ...")
                            user_password = input()

                            save_user(create_user(user_name,user_password)) # create and save new user.
                            print ('\n')
                            print(f" {user_name} user created")
                            print ('\n')
                    elif short_code == 'du':
                        if display_users():
                            print("Here is a list of all your users")
                            print("-"*10)
                            for user in display_users():
                                print(f"{user.user_name}")
                                print("-"*10)
                        else:
                            print('\n')
                            print("You don't seem to have any users saved yet")
                            print('\n')

                    elif short_code == 'li':

                        print("log into password vault account")
                        print("Enter the user name")
                        user_name = input()

                        print("Enter the password")
                        user_password = input()
                        if user_log_in(user_name,user_password) == None:
                            print("\n")
                            print("No account here,please create one")
                            print("\n")
                        else:

                            user_log_in(user_name,user_password)
                            print("\n")

                    elif short_code == "ex":
                        print("bye.....")
                        break
                    else:
                        print("I really didn't get that.Please use the short codes")
    while True:
                    print("Use these short codes : cc - create credentials, dc - display credentials, gp - generate password, ex -exit credentials")

                    short_code = input().lower()

                    if short_code == 'cc':

                        print("\n")
                        print("New credentials")
                        print("-"*10)

                        print("Name of credentials..")
                        credentials_name = input()
                        save_credentials(create_credentials(credentials_name, credentials_password))
                        # save_credentials( Credentials(user_password,  (create_generated_password(credentials_name)) ) )
                        print("\n")

                    elif short_code == "dc":
                        if display_credentials(user_password):
                            print("\n")
                            print(f"{user_name}")
                            print("-"*10)
                            for credentials in display_credentials(user_password):
                                print(f"Account...{crecredentials.credentials_name}")
                                print(f"password...{crecredentials.credentialscredentials_password}")
                                print("-"*10)
                        else:
                            print("\n")
                            print("No credentials found")
                            print("\n")
                    elif short_code == "gp":

                        print("\n")
                        print("New credentials")
                        print("-"*10)

                        print("Credential name is ....")
                        credentials_name = input()

                        save_credentials(Credentials(user_password,credentials_name,(create_generated_password(credcredentials_name))))
                        print("\n")
                        print(f"Credentials for {credentials_name} created and saved")

                    elif short_code == "ex":
                        print(f"bye{user_name}")
                        print("\n")

                    else:
                        print("\n")
                        print(f"{short_code} doesn't work")
                        print("\n")






if __name__ == '__main__':
    main()
