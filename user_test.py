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
        self.assertEqual(self.new_user.number,"0710283947")
        self.assertEqual(self.new_user.email,"shishnjonjo@gmail.com")

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
        test_user = User("Test","user","0710283947","test@user.com") #new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        """
        test_delete_user to test if we can remove a user from our user list
        """
        self.new_user.save_user()
        test_user = User("Test","user","0710283947","test@user.com")#new user
        test_user.save_user()

        self.new_user.delete_user()#Deleting a user object
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0710283974","test@user.com") # new user
        test_user.save_user()

        found_user = User.find_by_number("0710283974")

        self.assertEqual(found_user.email,test_user.email)
    def test_user_exist(self):
        """
        test to check whether we can return a Boolean if we cannot find the user
        """
        self.new_user.save_user()
        test_user = User("Test","user","0710283974","test@user.com") #new user
        test_user.save_user()

        user_exist = User.user_exist("0710283974")
        self.assertTrue(user_exist)

    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_users(),User.user_list)

if __name__ == '__main__':
    unittest.main()
