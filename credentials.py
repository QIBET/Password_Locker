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
    def delete_credential(self):
        '''
        Method to delete an object in the credential list
        '''
        Credentials.credential_List.remove(self)
    @classmethod
    def find_by_account(cls, account):
        '''
        Method that takes in an account and returns a credential that matches the account.

        Args:
            account: account to search for
        Returns :
            Contact of person that matches the number.
        '''
        for credential in cls.credential_List:
            if credential.account == account:
                return credential
    