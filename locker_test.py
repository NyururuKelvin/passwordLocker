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

def setUp(self):

    '''
    Set up method to run before each test cases.

    '''
    self.new_user = User("Kelvin", "Kelvin78") # create user object


def test_init(self):

    '''
    test_init test case to test if the object is initialized properly
    
    '''

    self.assertEqual(self.new_user.user_name, "Kelvin")
    self.assertEqual(self.new_user.password, "Kelvin78")
        