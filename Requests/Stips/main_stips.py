from time import sleep
import requests
import json
from color_printer import *
from Requests.Stips.A1_LoginStips import LoginStips
from Requests.Stips.A23_OnlineNotification import OnlineNotification

session = requests.session()

if __name__ == '__main__':
    print('Start')

    ### 1. Loging in user
    EMAIL = input('Please insert ur user email:') or  "idanb80@hotmail.com"
    PASS = input('Please insert ur user password:') or  "Idan05423"
    loginData = LoginStips(session, EMAIL, PASS) # This is not a func call. just set vars in class
    print(f'1. Login User...')
    LoginStips.login_stips(loginData)
    printYellow(f'User {EMAIL} logged in!')
    print('====================================================')

    loginData = OnlineNotification(session, EMAIL, PASS) # This is not a func call. just set vars in class
    notify_messages = input('2. Notify when new massages comes? (yes/no)') or 'yes'
    if notify_messages.lower() == 'yes':
        OnlineNotification.get_notifications(loginData, True)
        print('Ok. I will notify when new message come! [Available Soon..]')
    print('====================================================')

    notify_messages = input('3. Notify when some user online? (yes/no)') or 'yes'

    if notify_messages.lower() == 'yes':
        userId = input('Ok. Please enter the id of the user u like to follow:') or 337166
        OnlineNotification.check_online_user(loginData, userId)
        print('Ok. I will notify when this user online! [Available Soon..]')
    print('====================================================')


    print('4.Track Stips users activity based pen friends?')
    print('?? Ok. How many times a day should I Update u?')
    print('There was overall - 67 - massages from - 19 - users in the last 1 hour')