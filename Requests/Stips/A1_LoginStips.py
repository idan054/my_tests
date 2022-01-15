from time import sleep
import requests
import json
from color_printer import *

## Login stips (by cookies if possible)
## post pen message
## check for new private messages (get)

class LoginStips:
    # Set changeable Values: loginData = LoginStips(session, 'idan@', 'mypass')
    def __init__(self, session, user, password):
    # def __init__(self, user=10, password='idan default'):
        self.session = session
        self.userEmail = user
        self.password = password

    def set_new_cookie(self):
        session = self.session
        user = self.userEmail
        password = self.password

        # print("set_new_cookie()")
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
        open("config/stips_Cookies.txt", "w").write(_cookie[0])  # Overwrite
        open("config/stips_Cookies.txt", "a").write(f"\n{_cookie[1]}")  # adds to file

        return _cookie

    # Login by cookies if possible
    def login_stips(self):
        session = self.session
        user = self.userEmail
        password = self.password

        try:  # try logging by cookies
            cookieTXT_ls = open("config/stips_Cookies.txt", "r").read().splitlines()
            # print("cookieTXT: ", cookieTXT_ls)
            # ['Login%5FUser', 'ASPSESSIONIDQEQBTBAS']
            session.cookies.set("Login%5FUser", cookieTXT_ls[0])
            session.cookies.set("ASPSESSIONIDQEQBTBAS", cookieTXT_ls[1])
            printYellow("Logged in by Cookies 😋🍪")
            # print(session.cookies)
        except:
            printYellow("Baking new Cookies... 🥣🧑‍🍳")

            # create cookie for the session
            LoginStips.set_new_cookie(self)

        # api_data = LoginStips.get_api_data(self, True)  # return notificationsCount, messagesCount
        # if api_data[0] == 0 and api_data[1] == 0:
        #     printRed("Something went wrong with the current cookie... 🥴")
        #     printYellow("Baking new Cookies... 🥣🧑‍🍳")
        #     session.cookies.clear()
        #     LoginStips.set_new_cookie(self)
        #     api_data = LoginStips.get_api_data(self, True)  # re Set
    # login_stips(EMAIL, PASS)