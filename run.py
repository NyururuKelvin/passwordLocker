from locker import User
from locker import Credentials
import secrets
import string

def create_account(user_name, password):
    '''
    a function to create a new user account
    '''

    new_user = User(user_name, password)
    return new_user