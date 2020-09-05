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
    '''
    A function that saves credentials
    '''

    credentials.save_credentials()

def delete_credentials(credentials):
    '''
    A function that deletes credentials
    '''

    credentials.delete_credentials()

def find_credentials(account):
    '''
    A function that finds credentials by account and returns them
    '''

    return Credentials.find_by_account(account)

def check_existing_credentials(account):
    '''
    A function that checks if credentials exists with that account and returns a boolean
    '''

    return Credentials.credentials_exist(account)

def display_credentials():
    '''
    A function that returns saved credentials
    '''

    return Credentials.display_credentials()