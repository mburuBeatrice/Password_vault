# from user import User
# import pyperclip
from random import choice #This module generates a password
import string#This module also generates a password
class Credentials:

    """
    Class that generates new instances of credentials
    """

    def __init__(self,account_name,password):
        """
        __init__method helps us define properties for our objects.

        Args:
        name:New credentials account name.
        password:New credentials password.
        """
        self.account_name = account_name
        self.password = password

    credentials_list= [] # Empty credentials list
    def save_credentials(self):

        """
        save_user method saves user objects into user_list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method deletes a saved credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)
    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        Method that takes in an account_name and returns a password that matches that number.

        Args:
            account_name: Account name to search for
        Returns :
            credentials that matches the account name.
        '''

        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials
    @classmethod
    def credentials_exist(cls,account_name):
        """
        method that checks if a credential exists from a credentials list.

        Args:
           account_name: account name to search if it exists
        Return:
           Boolean: True or false depending if the credentials exists
        """
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return True
        return false
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    # @classmethod
    # def copy_email(cls,number):
    #     user_found = User.find_by_number(number)
    #     pyperclip.copy(user_found.email)
