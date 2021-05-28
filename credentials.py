class Credentials:
    '''
    User class to allows for creation of new instances of users
    '''
    def __init__(self,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            username: username for user.
            password: login password.
            
        '''
        self.username = username
        self.password = password