import unittest # imports unittest module
from user import User #imports the user Class

class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the user class behaviours.

    Args:
    unittest.TestCase: TestCase that helps in creating tset cases.

    """
    def setUp(self):

        """
        Set up method to run before each test case.
        """
        self.new_user = User("betty","njonjo","0710283947","shishnjonjo@gmail.com") # create user object

    def test_init(self):

        """
        test_init test case to test if the object is properly initialized
        """

        self.assertEqual(self.new_user.first_name,"betty")
        self.assertEqual(self.new_user.last_name,"njonjo")
        self.assertEqual(self.new_user.phone_number,"0710283947")
        self.assertEqual(self.new_user.email,"shishnjonjo@gmail.com")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into the user list
        """
        self.new_user.save_user() #save new user account
        self.assertEqual(len(User.user_list),1)
        
if __name__ == '__main__':
    unittest.main()
