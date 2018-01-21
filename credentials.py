# from user import User
class Credentials:

    """
    Class that generates new instances of credentials
    """
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
    credentials_list= [] # Empty credentials list
    def __init__(self,account_name,password):
        """
        __init__method helps us define properties for our objects.

        Args:
        name:New credentials account name.
        password:New credentials password.
        """
        self.account_name = account_name
        self.password = password
    def save_credentials(self):

        """
        save_user method saves user objects into user_list
        """
        Credentials.credentials_list.append(self)
