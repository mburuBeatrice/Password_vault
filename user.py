class User:

    """
    Class that generates new instances of users
    """

    user_list = [] # Empty user list
    def __init__(self,first_name,last_name,number,email):
        """
        __init__method helps us define properties for our objects.

        Args:
        first_name:New user first name.
        last_name:New user last name.
        number:New user phone number.
        email
        email:New user email address.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email




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
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a user that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            user that matches the number.
        '''

        for user in cls.user_list:
            if user.number == number:
                return user
    # @classmethod
    # def user_exist(cls,number):
    #     """
    #     method that checks if a user exists from a user list.
    #
    #     Args:
    #        number: Phone number to search if it exists
    #     Return:
    #        Boolean: True or false depending if the contact exists
    #     """
    #     for user in cls.user_list:
    #         if user.number == number
    #         returns True
    #     return false
