from user import User
class Credentials:

    """
    Class that generates new instances of credentials
    """

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
