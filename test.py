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
        self.new_user = User("Gabriel", "Odhiambo","0724835573","gabriel.odhiambo@ms.com", "Access")
