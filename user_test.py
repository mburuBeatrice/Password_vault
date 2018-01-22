import unittest # imports unittest module
from user import User #imports the user Class
from credentials import Credentials#imports the credentials Class
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
        self.new_user = User("betty","donkey1") # create user object

    def test_init(self):

        """
        test_init test case to test if the object is properly initialized
        """

        self.assertEqual(self.new_user.user_name,"betty")
        self.assertEqual(self.new_user.user_password,"donkey1")


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into the user list
        """
        self.new_user.save_user() #save new user account
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):

        """
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        """

        self.new_user.save_user()
        test_user = User("Test","donkey1") #new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        """
        test_delete_user to test if we can remove a user from our user list
        """
        self.new_user.save_user()
        test_user = User("Test","donkey1")#new user
        test_user.save_user()
    #
        self.new_user.delete_user()#Deleting a user object
        self.assertEqual(len(User.user_list),1)

    def test_find_credentials(self):
        '''
        test to check if a credential exists
        '''

        self.new_user.save_user()
        test_user = User("Test","donkey1") # new user
        test_user.save_user()

        found_credentials = User.find_credentials("Instagram")

        self.assertEqual(found_credentials,False)
    def test_log_in(self):
        """
        Test case to check if a user can log in credentials
        """
        self.new_user.save_user()
        test_user = User("Test","donkey1")
        test_user.save_user()
        found_credentials = User.log_in("Test","donkey1")
        self.assertEqual(found_credentials, Credentials.credentials_list)
    def test_user_exist(self):
        """
        test to check whether we can return a Boolean if we cannot find the user
        """
        self.new_user.save_user()
        test_user = User("Test","donkey") #new user
        test_user.save_user()

        user_exist = User.user_exist("Test")
        self.assertTrue(user_exist)

    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_users(),User.user_list)

if __name__ == '__main__':
    unittest.main(verbosity=2)
