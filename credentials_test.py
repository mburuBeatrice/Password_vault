import unittest # imports unittest module
from credentials import Credentials #imports the credentials Class

class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the credentials class behaviours.

    Args:
    unittest.TestCase: TestCase that helps in creating test cases.

    """
    def setUp(self):

        """
        Set up method to run before each test case.
        """
        self.new_credentials = Credentials("instagram","boo6254") # create credentials object

    def test_init(self):

        """
        test_init test case to test if the object is properly initialized
        """

        self.assertEqual(self.new_credentials.account_name,"instagram")
        self.assertEqual(self.new_credentials.password,"boo6254")

    Credentials.credentials_list = []

    def test_save_credentials(self):
        """
        test_save_credentials test case to test if the credentials object is saved into the credentials list
        """
        self.new_credentials.save_credentials() #save new credentials account
        self.assertEqual(len(Credentials.credentials_list),1)
if __name__ == '__main__':
    unittest.main()
