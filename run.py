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

def save_account(user):
    '''
    A function that saves a user
    '''

    User.create_account(user)

def login(user_name, password):
    '''
    A function that checks if a user exists and returns a  boolean
    '''

    return User.user_exist(user_name, password)

def create_credentials(account, username, password):
    '''
    A function that creates new credentials
    '''
    new_credentials = Credentials(account, username, password)
    return new_credentials

def save_credentials(credentials):
    pass