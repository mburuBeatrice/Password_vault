#!/usr/bin/env python3.6
from user import User
def create_user(fname,lname,phone,email):
    """
    Function to create a new user
    """
    new_user = User(fname,lname,phone,email)
    return new_user

def save_user(user):
    user.save_user

def delete_user(user):
    user.delete_user()

def find_user(number):
    return User.find_by_number

def check_existing_users(number):
    return User.user_list(number)

def display_users():
    return User.display_users()

def copy_email():
    return User.copy_email()

def main():
    print("Hello Welcome to your password locker.What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")

    print('\n')
    while True:
                    print("Use these short codes : cc - create a new user, dc - display users, fc -find a user, ex -exit the user list ")

                    short_code = input().lower()
if __name__ == '__main__':
    main()
