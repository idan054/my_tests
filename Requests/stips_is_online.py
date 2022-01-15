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

def telegram_printer(text):
    print("----------------------------")
    print("Also available on Telegram:")
    print(text)
    telegram_send.send(messages=[text])
    print("----------------------------")

while True:
    user_id, nickname, is_online = check_online_user(_id=online_user_id)

    print(f"\nLoop number: {while_index} | {str(while_index / 60)[:3]} hours past since launch")

    if is_online: online_status_text = "Online ✅"
    else: online_status_text = "Offline 🌚"

    if is_online != old_online_status:
        telegram_printer(f"User {user_id}, AKA {nickname} is currently {online_status_text}")
        old_online_status = is_online

    while_index += 1
    # sleep(60)

    #* 1 min loading bar
    for i in tqdm(range(60),
                  desc=Fore.GREEN + "Loading",
                  ascii=False, ncols=70, unit=""):
        time.sleep(1)
