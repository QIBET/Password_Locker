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
