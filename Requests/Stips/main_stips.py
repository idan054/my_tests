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
    ## Save email on cookies to make sure cookies is updated!
    EMAIL = input('Please insert ur user email:') or  "idanbit80+2@gmail.com"
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
    overall_pen_ids = []
    pen_stats = {
        'start_msgId' : 0,
        'finish_msgId' : 0,
        'msg_counter' : 0,
        'short_msg_length' : 70, # About 2 lines
        'short_msg_counter' : 0,
        'long_msg_counter' : 0,
        'overall_online_users' : 0,
        'male_online_user' : 0, # From profile user
        'female_online_user' : 0, # From profile user
        'returning_users' : 0, # From profile user - users who were active 4 times in the last 2 weeks
        'loyal_users' : 0, # From profile user - a 6+ month old users
    }
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
        pen_history ,pen_stats = StipsRoutinesTasks.get_pen_msgs(loginData, current_user_id, pen_history, pen_stats) # Save if its urs
    print('====================================================')

    ## 5. Save all pen messages stats? (overall msg & user count, gender)
    print('5.Track Stips users activity based pen friends?')
    printYellow('I will update next hour: \nHow many pen messages have been sent. \n& How many users have been online. [Available Soon..]')
    # get_penMsgs() # reset every hour & save every new user and msg id counter
    print('====================================================')

    # Add telegram_printer() with now(), to know the time in the console
    # Add a While True method to always run the needed funcs.

    while_index = 0
    while True:
        print('====================================================')
        print(f"Loop number: {while_index} | {str(while_index / 60)[:3]} hours past since launch")

        # Notify new messages
        if notify_messages: StipsRoutinesTasks.get_notifications(loginData, True),

        # Notify when specific user Online
        if notify_online:  StipsRoutinesTasks.check_online_user(loginData, userId) # Get full data of specific user

        # Save my pen messages history
        # Save all pen messages stats
        if save_ur_history_msgs: pen_history ,pen_stats = StipsRoutinesTasks\
            .get_pen_msgs(loginData, current_user_id, pen_history, pen_stats, overall_pen_ids) # Save if its urs


        print('====================================================') # userId isn't set if not notify_online



        # sleep(60)
        while_index += 1
        # * 1 min loading bar
        for i in tqdm(range(10),
                      desc=Fore.GREEN + "Loading",
                      ascii=False, ncols=70, unit=""):
            time.sleep(1)

