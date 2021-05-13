import requests
import json

# EMAIL =
EMAIL = "Idanb80@gmail.com"
PASS = "Idan05423"

session = requests.session()

def get_new_cookie(user, password):
    print("get_new_cookie()")
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
    api_params = json.dumps(api_params)  # dumps for " (Double ')

    payload = {
        "name": "user.login",
        "api_params": api_params
    }
    print()
    login_res = session.get("https://stips.co.il/api", data=payload)
    # print(login_res.status_code)
    # print("login_res", login_res.content)

    _cookie = login_res.headers["Set-Cookie"]
    print(_cookie)
    # _cookie = "Login%5FUser=stype=75r4&password=Vqn0DIHFG&id=EGMGFJ&mail=vqn0oLD%40tznvy%2Ep1z&rememberme=true; expires=Tue, 02-May-2023 23:52:02 GMT; domain=.stips.co.il; path=/"
    open("Cookie.txt", "w").write(_cookie)

    return _cookie
# Set the cookie for the session

def data_based_cookie(isPrintingTime):
    print("data_based_cookie()")
    # Remember: the cookie already embed in the sesssion

    # Cookies has been set by the session
    res = session.get("https://stips.co.il/api?name=messages.count&api_params=%7B%7D")
    print(res.text)
    res_dict = json.loads(res.text)
    notificationsCount = res_dict["data"]["notificationsCount"]
    messagesCount = res_dict["data"]["messagesCount"]
    if isPrintingTime:
        print("notificationsCount is", notificationsCount)
        print("messagesCount is", messagesCount)
    return notificationsCount, messagesCount


print("Check if current cookie is tasty...")
# cookie = open("Cookie.txt", "r").read()
cookie = "Login%5FUser=stype=75r4&password=Vqn0DIHFG&id=EGMGFJ&mail=vqn0oLD%40tznvy%2Ep1z&rememberme=true; expires=Tue, 02-May-2023 23:52:02 GMT; domain=.stips.co.il; path=/"
print(session.cookies)
# session.cookies.set("Set-Cookie", cookie)
print(session.cookies)

if data_based_cookie(True)[0] == 0 \
    and data_based_cookie(True)[1] == 0:

    print("Well, i'll bake new cookie...")
    cookie = get_new_cookie(EMAIL, PASS)
    print("New cookie is ready!")
else:
    print("Current cookie is great!")

print(cookie)
print(session.cookies)
data_based_cookie(True)



