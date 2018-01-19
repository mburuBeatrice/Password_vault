class User:

    """
    Class that generates new instances of users
    """
def __init__(self,first_name,last_name,phone_number,email):
    """
    __init__method helps us define properties for our objects.

    Args:
    first_name:New user first name.
    last_name:New user last name.
    phone_number:New user phone number.
    email
    email:New user email address.
    """
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email
