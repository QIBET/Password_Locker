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
    def test_create_user(self):
        '''
        Test to check whether a user is created successfully
        '''
        self.assertEqual(self.new_user.first_name,"Gabriel")
        self.assertEqual(self.new_user.last_name,"Odhiambo")
        self.assertEqual(self.new_user.phone_number,"0724835573")
        self.assertEqual(self.new_user.email,"gabriel.odhiambo@ms.com") 
        self.assertEqual(self.new_user.password,"Access")

        
if __name__ == '__main__':
    unittest.main()

