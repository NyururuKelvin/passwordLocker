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

def test_create_account(self):

    '''
    test_create_account test case to test if the user object is saved into
    the user list

    '''

    self.new_user.create_account()
    self.assertEqual(len(User.users_list), 1)

def test_save_multiple_accounts(self):

    '''
    test_save_multiple_user to check if we can save multiple users
    objects to our user_list
    
    '''

    self.new_user.create_account()
    test_user = User("Amimo", "Amimo78") #new user
    test_user.create_account()
    self.assertEqual(len(User.users_list), 2)
        