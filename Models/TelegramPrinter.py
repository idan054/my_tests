from time import sleep
import requests
import json
# from color_printer import *
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

def telegram_printer(text):
    # print("----------------------------")
    print("Also available on Telegram!")
    # print(text)
    telegram_send.send(messages=[text])
    print("----------------------------")