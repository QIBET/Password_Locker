#!/usr/bin/env python3.6
from user import User
from credentials import Credentials 

def create_user(f_name,l_name,phone,email,password):
    '''
    function to create contact
    '''
    new_user = User(f_name,l_name,phone,email,password)
    return new_user
def save_users(user):
    '''
    Function to save user instance
    '''
    user.save_user()
def create_credential(account,username,password):
    '''
    Function to create user credentials
    '''
    new_credential = Credentials(account,username,password)
    return new_credential
def save_credential(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials(credentials)
def del_credential(credentials):
    '''
    Function to implement the delete method
    '''
    credentials.delete_credential(credentials)
def find_credential(account):
    '''
    Function to return credential using account
    '''
    return Credentials.find_by_account(account)

def display_credential():
    '''
    Function to display credentials
    '''
    return Credentials.display_credentials()
def generate_password():
    '''
    Function to generate random password
    '''
    Credentials.password_generator()
def main():
    '''
    Initializing the main function
    '''
    print("Hello welcome to your Password Locker Account")
    print('\n')
    shortcode = input("Kindly enter cc to sign up?")
    print('\n')
    while shortcode != "cc":
    
        print("Invali Input, Kindly enter su to sign up ")
        shortcode = input("Kindly enter su to sign up?")
    else:
        firstName = input("Enter firstname:")
        print ('\n')
        lastName = input("Enter lastname:")
        print ('\n')
        phoneNumber = input("Enter phone number:")
        print ('\n')
        email = input("Enter email:")
        print ('\n')
        password = input("Enter password: ")

        
        save_users(create_user(firstName,lastName,phoneNumber,email,password))
        print(f"Hello {firstName} you have succesfully created an account")
        while True:
             print("Use these short codes: cc - Create new credentials, dc - display credentials, fc  - find credentials, ex - exit the enviironment, del - delete a credential")
             short_code = input().lower() 
             if short_code == 'cc':
                print('NEW CREDENTIALS')   
                print("*" * 20)

                print("Account Name: ")
                print ('\n')
                account_Name = input()

                print("Username:")
                print ('\n')
                user_name = input()

                print("Password:")
                credential_id = input()

                save_credential(create_credential(account_Name,user_name,credential_id))
                print ('\n')
                print(f"Hello {account_Name} account has been succesfully created")
                print("\n")
             elif short_code == 'dc':
                if display_credential():
                    print("Here is a list of all your Credentials")
                    print('\n')
                    for credential in display_credential():
                        print(f"{credential.account} {credential.username}  {credential.password}")
                    print("\n")
                else:
                    print("\n")
                    print("You do not seem to have any credential account yet!!")
                    print("\n")




if __name__ == '__main__':
    main()
        
