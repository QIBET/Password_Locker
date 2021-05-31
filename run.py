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
    credentials.save_credentials()
def del_credential(credentials):
    '''
    Function to implement the delete method
    '''
    credentials.delete_credential()
def find_credential(account):
    '''
    Function to return credential using account
    '''
    return Credentials.find_by_account(account)
def trace_existing_account(account):
    '''
    check the existence of an account
    '''
    return Credentials.credential_exist(account)
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
    shortcode = input("Kindly enter su to sign up?")
    print('\n')
    while shortcode != "su":
    
        print("Invali Input, Kindly enter su to sign up ")
        shortcode = input("Kindly enter su to sign up?")
        print('\n')
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

                print("Enter Account Name: ")
              
                account_Name = input()

                print("Enter Username:")
            
                user_Name = input()

                print("Do you want to use a system generated Password? Type Yes or No: ")
                password = input()
                if password == 'yes':
                    credential_Id = generate_password()
                else:
                    print("Enter Password:")
                    credential_Id = input()

                save_credential(create_credential(account_Name,user_Name,credential_Id))
                print ('\n')
                print(f"Hello, your {account_Name} account has been succesfully created")
                print("\n")
             elif short_code == 'dc':
                if display_credential():
                    print("Here is a list of all your Credentials")
                    print('\n')
                    for credential in display_credential():
                        print(f"Account Name: {credential.account}")
                        print("-" * 10)
                        print(f"Username: {credential.username}")
                        print("-" * 10)
                        print(f"Password: {credential.password}")
                    print("\n")
                else:
                    print("\n")
                    print("You do not seem to have any credential account yet!!")
                    print("\n")
             elif short_code == "fc":
                print("Please enter the account name you would like to search")
                    
                search_account_name = input()
                if trace_existing_account(search_account_name):
                    found_credential = find_credential(search_account_name)
                    print("\n")
                    print(f"Account Name: {found_credential.account}")
                    print("-" * 10)
                    print("\n")
                    print(f"Username:{found_credential.username}")
                    print("\n")
                    print(f"Password:  {found_credential.password}")
                else:
                    print("The account isn't existent")
             elif short_code == 'del':
                print("You are about to delete an Account!!")
                account = input("Kindly search a credential to delete using an account ")
                if del_credential(find_credential(account)):
                    print("Account deleted successfully")
                else:
                    print("Kindly select a different option")

             elif short_code == 'ex':
                print("au revoir")
                break
             else:
                print("Ensure you input a shortcode")




if __name__ == '__main__':
    main()
        
