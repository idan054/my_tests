from time import sleep
import requests
import json
from color_printer import *

from Models.TelegramPrinter import telegram_printer
from Requests.Stips.A_LoginStips import LoginStips
from Requests.Stips.B_StipsRoutinesTasks import StipsRoutinesTasks
from time import sleep
import requests
import json
from tqdm import tqdm
from colorama import Fore, Back, Style
import time
import sys
# from color_printer import *
import datetime
from time import sleep
import telegram_send

session = requests.session()

if __name__ == '__main__':
    print('Start')

    ## 1. Loging user
    EMAIL = input('Please insert ur user email:') or  "idanb80@hotmail.com"
    PASS = input('Please insert ur user password:') or  "Idan05423"
    loginData = LoginStips(session, EMAIL, PASS) # This is not a func call. just set vars in class
    print(f'1. Login User...')
    current_user_id = LoginStips.login_stips(loginData)
    # region Note: (optionally) get full user data by profile page & user id
    # currentUserData = {
    #     'id': 337166,
    #     'nickname': 'האמתשלי',
    #     'gender': 1,
    #     'has_photo': True,
    # }
    # endregion Can run here profile page to get full data based id
    printYellow(f'User {EMAIL} logged in!')
    print('====================================================')


    ## 2. Notify new messages?
    loginData = StipsRoutinesTasks(session, EMAIL, PASS) # This is not a func call. just set vars in class
    notify_messages = input('2. Notify when new massages comes? (yes/no)') or 'yes'
    if notify_messages.lower() == 'yes':
        printYellow('I will notify when new message come! [Available Soon..]')
        StipsRoutinesTasks.get_notifications(loginData, True)
    print('====================================================')


    ## 3. Notify when specific user Online?
    notify_online = input('3. Notify when some user online? (yes/no)') or 'yes'
    if notify_online.lower() == 'yes':
        userId = input('Ok. Please enter the id of the user u like to follow:') or 337166
        printYellow('I will notify when this user online! [Available Soon..]')
        StipsRoutinesTasks.check_online_user(loginData, userId) # Get full data of specific user
    print('====================================================')


    ## 4. Save my pen messages history?
    pen_history = []
    # pen_history = {'data': []}
    #   pen_history = [  {
    #   'msg_id': 5916290,
    #   'msg_content': 'היי',
    #   'user_id': 321654,
    #   'user_nickname': 'LadyWinx',
    #   'time_str': 321654
    # }]
    save_ur_history_msgs = input('4. Save ur pen messages history? (yes/no)') or 'yes'
    if save_ur_history_msgs.lower() == 'yes':
        printYellow('I will save ur pen messages history! [Available Soon..]')
        #         printGreen('[MOCK] Ur pen messages history: (3) \nאחי זה הכי אחי\nאם תרצו אין זו אגדה באדוקק')
        pen_history = StipsRoutinesTasks.get_pen_msgs(loginData, current_user_id, pen_history) # Save if its urs
    print('====================================================')

    ## 4. Save all pen messages stats? (overall msg & user count, gender)
    print('5.Track Stips users activity based pen friends?')
    printYellow('I will update next hour: \nHow many pen messages have been sent. \n& How many users have been online. [Available Soon..]')
    # get_penMsgs() # reset every hour & save every new user and msg id counter
    printGreen('There was overall - 67 - pen massages from - 19 - users in the last 1 hour')
    print('====================================================')

# Add telegram_printer() with now(), to know the time in the console
# Add a While True method to always run the needed funcs.

while_index = 0
while True:
    print(f"\nLoop number: {while_index} | {str(while_index / 60)[:3]} hours past since launch")

    # user_id, nickname, is_online = check_online_user(_id=online_user_id)
    #
    #
    # if is_online: online_status_text = "Online ✅"
    # else: online_status_text = "Offline 🌚"
    #
    # if is_online != old_online_status:
    #     telegram_printer(f"User {user_id}, AKA {nickname} is currently {online_status_text}")
    #     old_online_status = is_online

    while_index += 1
    sleep(60)

    #* 1 min loading bar

    # for i in tqdm(range(60),
    #               desc=Fore.GREEN + "Loading",
    #               ascii=False, ncols=70, unit=""):
    #     time.sleep(1)