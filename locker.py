class User:

    """
    Class that generates new instances of users

    """
    
    users_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

class Credentials:

    """
    Class that generates new instances of credentials

    """

    credentials_list = []

    def __init__(self, account, username, password):

        '''
        __init__ method that helps us define properties for our objects.
        
        Args:
            account: New credentials account name.
            username : New credentials password.
            password: New credentials password.
           
        '''

        self.account = account
        self.username = username
        self.password = password