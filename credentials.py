class Credentials:
    '''
    User class to allows for creation of new instances of users
    '''
    credential_List = []

    def __init__(self,account,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account: account being saved by user
            username: username for user.
            password: login password.
            
        '''
        self.account = account
        self.username = username
        self.password = password
    def save_credentials(self):
        '''
        Method to save credentials
        '''
        Credentials.credential_List.append(self)
    