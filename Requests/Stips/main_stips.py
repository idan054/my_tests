from time import sleep
import requests
import json
from color_printer import *
from Requests.Stips.login_stips import LoginStips


session = requests.session()
if __name__ == '__main__':
    print('Start')

    ### 1. Loging in user
    EMAIL = input('Please insert ur user email:') or  "idanb80@hotmail.com"
    PASS = input('Please insert ur user password:') or  "Idan05423"
    loginData = LoginStips(session, EMAIL, PASS)
    print(f'1. Login User {EMAIL}...')
    LoginStips.login_stips(loginData)
    print('User EMAIL logged in')
    print('====================================================')

    print('2. Notify when new massages comes?')
    print('User X Have X massages & X notifications.')

    print('3. Notify when some user online?')
    print('?? Ok. Please enter the id of the user u like to follow:')
    print('User 337166, AKA  "The Biton" is currently Online ✅')
    # print('User 337166, AKA  "The Biton" is currently Offline 🌚')

    print('4.Track Stips users activity based pen friends?')
    print('?? Ok. How many times a day should I Update u?')
    print('There was overall - 67 - massages from - 19 - users in the last 1 hour')