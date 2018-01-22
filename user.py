
from credentials import Credentials#import credential module to access an account's credentials
class User:

    """
    Class that generates new instances of users
    """

    user_list = [] # Empty user list
    def __init__(self,user_name,user_password):
        """
        __init__method helps us define properties for our objects.

        Args:
        user_name:New user first name.
        user_password:New user last name.
        """
        self.user_name = user_name
        self.user_password = user_password





    def save_user(self):

        """
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        delete_user method deletes a saved user from the user_list
        """

        User.user_list.remove(self)
    @classmethod
    def find_credentials(cls,name):
        '''
        Method that takes in a name and checks corresponding credentials.

        Args:
            name: credentials name to search for
        Returns :
        Boolean: returns true/false if the credentials exists
        '''

        for credentials in Credentials.credentials_list:
            if credentials.credentials_name == name:
                return True

        return False
    @classmethod
    def log_in(cls, name, password):
        """
        method that allows user to log into credentials

        Args:
        name:nameof the user
        password:password of the user

        Returns:
        Credentials listfor the user that matches the name and password
        False:name or password is incorrect
        """
        for user in cls.user_list:
            if user.user_name == name and user.user_password == password:
                return Credentials.credentials_list
        return False


    @classmethod
    def user_exist(cls,name):
        """
        method that checks if a user exists from a user list.

        Args:
           name: user name to search if it exists
        Return:
           Boolean: True or false depending if the contact exists
        """
        for user in cls.user_list:
            if user.user_name == name:
                return True
        return false
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
