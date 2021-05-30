from random import randint
import random
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
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials in full
        '''
        return cls.credential_List
    @classmethod
    def credential_exist(cls,account):
        '''
        method that checks the existence of an object
        arguements:
            Account name to search if it exists
        returns:
            boolean:true or false based on result
        '''
        for findaccount in cls.credential_List:
            if findaccount.account== account:
                return True
        return False

password_generated = []
lettersList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
'''
converting lettersList strings to uppercase
'''
lettersListUpper = []

for item in lettersList:
    letter = item.upper()
    lettersListUpper.append(letter)

  

    def password_generator():
        
        password_generated_sliced = ''
        for range in lettersList:
            range = randint(0, 100)
            if range%2 == 0:
                password_generated.append(random.choice(lettersList))
            elif range%5==0 or range%3 == 0:
                password_generated.append(random.choice(lettersListUpper))
            else:
                password_generated.append(str(range))

        password_generated_sliced = password_generated[0:8:1]
        random_password=(''.join(password_generated_sliced))

        print(f'your password is: {random_password}')

        return random_password