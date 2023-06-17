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

telegram_printer("LOL")
## Login stips (by cookies if possible)
## post pen message
## check for new private messages (get)

# EMAIL =
EMAIL = "idanb80@gmail.com"
PASS = "Idan05423"

session = requests.session()

# create cookie for the session
def set_new_cookie(user, password):
    print("set_new_cookie()")
    # load as dict for easy edit values
    api_params = json.loads(
        """{
        "email": "Placeholder",
        "password": "Placeholder",
        "auth_token": ""
        }"""
    )
    api_params["email"] = user
    api_params["password"] = password

    # print(api_params)
    api_params = json.dumps(api_params)  # dumps to change ' to "


    payload = {
        "name": "user.login",
        "api_params": api_params
    }
    login_res = session.get("https://stips.co.il/api", data=payload)
    # print(type(session.cookies))
    # print(login_res.status_code)
    # print("login_res", login_res.content)

    # _cookie = response.headers["Set-Cookie"]
    _cookie = session.cookies.values()
    # _cookie = "Login%5FUser=stype=75r4&password=Vqn0DIHFG&id=EGMGFJ&mail=vqn0oLD%40tznvy%2Ep1z&rememberme=true; expires=Tue, 02-May-2023 23:52:02 GMT; domain=.stips.co.il; path=/"
    open("../config/stips_Cookies.txt", "w").write(_cookie[0]) # Overwrite
    open("../config/stips_Cookies.txt", "a").write(f"\n{_cookie[1]}") # adds to file


    return _cookie

# Make a session request to get data
def get_api_data(isPrinting):
    print("get_api_data()")
    # Remember: the cookie already embed in the sesssion

    # Cookies has been set by the session
    res = session.get("https://stips.co.il/api?name=messages.count&api_params=%7B%7D")
    res_dict = json.loads(res.text)
    notificationsCount = res_dict["data"]["notificationsCount"]
    messagesCount = res_dict["data"]["messagesCount"]
    if isPrinting:
        # printBlue(res.text)
        print(res.text)
    return notificationsCount, messagesCount

# Login by cookies if possible
def login_stips():
    try:  # try logging by cookies
        cookieTXT_ls = open("../config/stips_Cookies.txt", "r").read().splitlines()
        # print("cookieTXT: ", cookieTXT_ls)
        # ['Login%5FUser', 'ASPSESSIONIDQEQBTBAS']
        session.cookies.set("Login%5FUser", cookieTXT_ls[0])
        session.cookies.set("ASPSESSIONIDQEQBTBAS", cookieTXT_ls[1])
        # printYellow("Logged in by Cookies 😋🍪")
        print("Logged in by Cookies 😋🍪")
        # print(session.cookies)
    except:
        # printYellow("Baking new Cookies... 🥣🧑‍🍳")
        print("Baking new Cookies... 🥣🧑‍🍳")
        set_new_cookie(EMAIL, PASS)

    api_data = get_api_data(True)  # return notificationsCount, messagesCount
    if api_data[0] == 0 and api_data[1] == 0:
        # printRed("Something went wrong with the current cookie... 🥴")
        # printYellow("Baking new Cookies... 🥣🧑‍🍳")
        print("Something went wrong with the current cookie... 🥴")
        print("Baking new Cookies... 🥣🧑‍🍳")
        session.cookies.clear()
        set_new_cookie(EMAIL, PASS)
        api_data = get_api_data(True)  # re Set

    # printGreen(f"🔔 notificationsCount is {api_data[0]}")
    # printGreen(f"📱 messagesCount is {api_data[1]}")
    print(f"🔔 notificationsCount is {api_data[0]}")
    print(f"📱 messagesCount is {api_data[1]}")
    print("---------------------------")
login_stips()

def check_online_user(_id):
    from pprint import pprint
    # response = session.get('https://stips.co.il/api?name=omniobj&rest_action=GET&omniobj={"objType":"user","data":{"id":146235}}')

    mini_payload = {
          "objType": "user",
          "data": {
            "id": 000000
          }
}

    mini_payload["data"]["id"] = _id
    mini_payload = str(mini_payload)
    # print(mini_payload)

    url = f'https://stips.co.il/api?name=omniobj&rest_action=GET&omniobj={str(mini_payload)}'.replace("'", '"')
    # print(url)
    # url = 'https://stips.co.il/api?name=omniobj&rest_action=GET&omniobj={"objType":"user","data":{"id":146235}}'
    # print(url)

    response = session.get(url)
    # pprint(response.content)
    user_data = json.loads(response.content)
    _user_id = user_data["data"]["omniOmniObj"]["data"]["id"]
    _nickname = user_data["data"]["omniOmniObj"]["data"]["nickname"]
    _is_online = user_data["data"]["omniOmniObj"]["extra"]["item_profile"]["online"]
    return _user_id, _nickname, _is_online

global pen_msgs
def get_pen_msgs():
    global pen_msgs
    from pprint import pprint
    # response = session.get('https://stips.co.il/api?name=objectlist&api_params=%7B%22method%22:%22penfriendsitem.new%22,%22page%22:1%7D')
    response = session.get('https://stips.co.il/api?name=objectlist&api_params={"method":"penfriendsitem.new","page":1}')
    # pprint(response.status_code)
    # pprint(response.text)
    pen_msgs = json.loads(response.text)
    # pen_userid = pen_msgs["data"][msg_index]["data"]["userid"]
    # pen_msg = pen_msgs["data"][msg_index]["data"]["msg"]
    # pen_nickname = pen_msgs["data"][msg_index]["extra"]["item_profile"]["nickname"]
    return pen_msgs

old_online_status  = "PlaceHolder"
online_status_text = ""
while_index = 1
selected_user_id = input("Please insert the stips user id:") or 139326 # AKA TheBiton
my_pen_msgs = []
while True:
    pen_msgs = get_pen_msgs()
    # print(pen_msgs)
    forIndex = 0
    for msg in pen_msgs:
        pen_userid = pen_msgs["data"][forIndex]["data"]["userid"]
        pen_msg = pen_msgs["data"][forIndex]["data"]["msg"]
        pen_nickname = pen_msgs["data"][forIndex]["extra"]["item_profile"]["nickname"]

        if pen_userid == selected_user_id and pen_msg not in my_pen_msgs:
            # print(pen_userid)
            # print(pen_msg)
            # print(pen_nickname)
            # print("forIndex:", forIndex)
            # print("forIndex:", forIndex)
            telegram_printer(text=f"המסר בסטיפס: \n {pen_msg}")
            my_pen_msgs.append(pen_msg)
        else:
            print(forIndex, "|" , pen_userid, "!=", selected_user_id)
            # print(pen_msg)
            # print(pen_nickname)

        forIndex += 1
    print(len(pen_msgs))

    print(f"\nLoop number: {while_index} | {str(while_index / 6)[:3]} Minutes past since launch")

    while_index += 1
    # sleep(60)

    #* 1 min loading bar
    for i in tqdm(range(30),
                  desc=Fore.GREEN + "Loading",
                  ascii=False, ncols=70, unit=""):
        time.sleep(1)
