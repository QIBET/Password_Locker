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