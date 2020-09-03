import unittest
from locker import User
from locker import Credentials
import pyperclip

class TestUsers(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

def tearDown(self):

    '''
        tearDown method to run after each test  cases.
        '''
        User.users_list = []