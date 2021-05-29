import unittest
from user import User
from credentials import Credentials 

class Testclass (unittest.TestCase):
    '''
    Test class that defines test cases for the user/credentials class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Gabriel", "Odhiambo","0724835573","gabriel.odhiambo@ms.com", "Access")#first user object
        self.new_credential = Credentials("facebook","admin","Access") #first credential object
    def tearDown(self):
        '''
        clears the counter after every test
        '''
        Credentials.credential_List = []
    def test_create_user(self):
        '''
        Test to check whether a user is created successfully
        '''
        self.assertEqual(self.new_user.first_name,"Gabriel")
        self.assertEqual(self.new_user.last_name,"Odhiambo")
        self.assertEqual(self.new_user.phone_number,"0724835573")
        self.assertEqual(self.new_user.email,"gabriel.odhiambo@ms.com") 
        self.assertEqual(self.new_user.password,"Access")
    def test_save_user(self):
        '''
        test to check whether user details are saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_List),1)
    def test_create_credentials(self):
        '''
        test to check whether a new instance of credentials can be created
        '''
       

        self.assertEqual(self.new_credential.account,"facebook")
        self.assertEqual(self.new_credential.username,"admin")
        self.assertEqual(self.new_credential.password,"Access")
    def test_save_credentials(self):
        '''
        test to check whether user credentials are saved
        '''
        self.new_credential = Credentials("facebook","admin","Access")

        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_List),1)
    def test_save_multiple_credentials(self):
         '''
         test to check for ability to save multiple credentials
         '''
         self.new_credential.save_credentials()
         test_credential = Credentials("gmail", "ghettoboy","Moringa2021")#new credential
         test_credential.save_credentials()
         self.assertEqual(len(Credentials.credential_List),2)
    def test_delete_credential(self):
        '''
        test whether an object is deleted
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("gmail", "ghettoboy","Moringa2021")#deleting an object
        test_credential.save_credentials()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credential_List),1)
    def test_find_credential_by_account(self):
        '''
        find a credential object using the account
        '''
        self.new_credential.save_credentials()
        search_credential = Credentials("Yahoo","kbenniez", "Nai2021")
        search_credential.save_credentials()
        
        found_credential = Credentials.find_by_account("Yahoo")
        self.assertEqual(found_credential.username,search_credential.username)
    def test_display_credentials(self):
        '''
        method to display user credentials
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credential_List)

        
if __name__ == '__main__':
    unittest.main()

