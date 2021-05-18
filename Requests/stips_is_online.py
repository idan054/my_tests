from time import sleep
import requests
import json
# from color_printer import *

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
