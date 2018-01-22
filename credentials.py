# from user import User
import pyperclip
from random import choice #This module generates a credentials_password
import string#This module also generates a credentials_password
class Credentials:

    """
    Class that generates new instances of credentials
    """

    def __init__(self,user_password,credentials_name,credentials_password):
        """
        __init__method helps us define properties for our objects.

        Args:
        user_password:password of the user
        credentials_name:New credentials credentials_name.
        credentials_password:New credentials credentials_password.
        """
        self.user_password = user_password
        self.credentials_name = credentials_name
        self.credentials_password = credentials_password

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
    def generate_password(self):
        """
        method that generates a random alphanumeric password
        """
        size = 7 #length of generated password
        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase #generate random alphanumeric
        password = ''.join(choice(alphanum) for num in range(size))
        return password

    @classmethod
    def find_by_credentials_name(cls,name):
        '''
        Method that takes in an credentials_name and returns a credentials_password that matches that number.

        Args:
            credentials_name: credentials name to search for
        Returns :
            credentials that matches the account name.
        '''

        for credentials in cls.credentials_list:
            if credentials.credentials_name == name:
                return credentials
    @classmethod
    def credentials_exist(cls,name):
        """
        method that checks if a credential exists from a credentials list.

        Args:
           credentials_name: account name to search if it exists
        Return:
           Boolean: True or false depending if the credentials exists
        """
        for credentials in cls.credentials_list:
            if credentials.credentials_name == name:
                return True
        return false
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    @classmethod
    def copy_credentials(cls,number):
        credentials_found = Credentials.find_by_credentials_name(name)
        pyperclip.copy(credentials_found.name)
