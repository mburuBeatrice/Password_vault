import unittest # imports unittest module
from credentials import Credentials #imports the credentials Class

class TestCredentials(unittest.TestCase):

    """
    Test class that defines test cases for the credentials class behaviours.

    Args:
    unittest.TestCase: TestCase that helps in creating test cases.

    """
    def setUp(self):

        """
        Set up method to run before each test case.
        """
        self.new_credentials = Credentials("betty","instagram","boo6254") # create credentials object

    def test_init(self):

        """
        test_init test case to test if the object is properly initialized
        """
        self.assertEqual(self.new_credentials.user_password,"betty")
        self.assertEqual(self.new_credentials.credentials_name,"instagram")
        self.assertEqual(self.new_credentials.credentials_password,"boo6254")
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list= []

    def test_save_credentials(self):
        """
        test_save_credentials test case to test if the credentials object is saved into the credentials list
        """
        self.new_credentials.save_credentials() #save new credentials account
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):

        """
        test_save_multiple_credentials to check if we can save multiple credentials objects to our credentials_list
        """

        self.new_credentials.save_credentials()
        test_credentials = Credentials("shiru","facebook","donkey124") #new credentials
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        """
        test_delete_credentials to test if we can remove a credentials from our credentials list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("user_password","credentials_name","credentials_password")#new credentials
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()#Deleting a credentials object
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_generate_password(self):
        """
        test if a user can log in
        """
        generated_password = self.new_credentials.generate_password()
        self.assertEqual(len(generated_password), 7)

    def test_find_credentials_by_credentials_name(self):
        '''
        test to check if we can find a credential by account name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("cookie","x_account","88888") # new credentials
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_credentials_name("x_account")
    def test_credentials_exist(self):
        """
        test to check whether we can return a Boolean if we cannot find the credentials
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("cookie","x_account","88888") #new credentials
        test_credentials.save_credentials()

        credentials_exist = Credentials.credentials_exist("x_account")
        self.assertTrue(credentials_exist)

    def test_display_all_credentials(self):
        """
        method that returns a list of all credentials saved
        """
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main(verbosity=2)
