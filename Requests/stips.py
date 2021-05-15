from time import sleep
import requests
import json
from color_printer import *

## Login stips (by cookies if possible)
## post pen message
## check for new private messages (get)

# EMAIL =
EMAIL = "idanb80@hotmail.com"
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
    open("../StipsCookies.txt", "w").write(_cookie[0]) # Overwrite
    open("../StipsCookies.txt", "a").write(f"\n{_cookie[1]}") # adds to file


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
        printBlue(res.text)
    return notificationsCount, messagesCount


# Login by cookies if possible
def login_stips():
    try:  # try logging by cookies
        cookieTXT_ls = open("../StipsCookies.txt", "r").read().splitlines()
        # print("cookieTXT: ", cookieTXT_ls)
        # ['Login%5FUser', 'ASPSESSIONIDQEQBTBAS']
        session.cookies.set("Login%5FUser", cookieTXT_ls[0])
        session.cookies.set("ASPSESSIONIDQEQBTBAS", cookieTXT_ls[1])
        printYellow("Logged in by Cookies 😋🍪")
        # print(session.cookies)
    except:
        printYellow("Baking new Cookies... 🥣🧑‍🍳")
        set_new_cookie(EMAIL, PASS)

    api_data = get_api_data(True)  # return notificationsCount, messagesCount
    if api_data[0] == 0 and api_data[1] == 0:
        printRed("Something went wrong with the current cookie... 🥴")
        printYellow("Baking new Cookies... 🥣🧑‍🍳")
        session.cookies.clear()
        set_new_cookie(EMAIL, PASS)
        api_data = get_api_data(True)  # re Set

    printGreen(f"🔔 notificationsCount is {api_data[0]}")
    printGreen(f"📱 messagesCount is {api_data[1]}")
    print("---------------------------")
login_stips()

# Response: {"status":"ok","error_code":"","data":{"newid":4909228},"exec_time":"86ms"}
def post_pen_msg(msg):

    # payload = {
    #     "name": "omniobj",
    #     "rest_action": "PUT",
    #     "omniobj": """{
    #       "data": {
    #         "msg": "Bruh3"
    #       },
    #       "objType": "penfriendsitem"
    #     }"""
    # }

    full_payload = json.loads("""{
        "name": "omniobj",
        "rest_action": "PUT",
        "omniobj": {
        "data": { "msg": "PlaceHolder" },
          "objType": "penfriendsitem"
            }
        }""")

    full_payload["omniobj"]["data"]["msg"] = msg
    full_payload["omniobj"] = str(full_payload["omniobj"]).replace("'", '"')
    # full_payload["omniobj"] = json.dumps(full_payload)  # dumps to change ' to "

    response = session.post("https://stips.co.il/api", data=full_payload)
    # response = session.post("https://stips.co.il/api?name=omniobj&rest_action=PUT&omniobj=%7B%22data%22:%7B%22msg%22:%22BRUH3%22%7D,%22objType%22:%22penfriendsitem%22%7D")
    # print(response.status_code)
    # print(response.content)

    pen_msg_id = json.loads(response.content)["data"]["newid"]
    # print(pen_msg_id) # 0 if failed

    return pen_msg_id

# pen_msg_id = post_pen_msg("תתעלמו ממני, אני בכלל לא עושה בדיוק תדבר הכי מגניב שיש (האמנם?)")
pen_msg_id = post_pen_msg("סמיילי מאוהב")
if pen_msg_id != 0: printGreen("✅ Message has been sent.")
else: printRed("️Message has not sent❗ \nPlease try again later..")
print("---------------------------")

new_messages = ["PlaceHolder"]
whileIndex = 0
while True:
    # response = session.get("https://stips.co.il/api?name=messages.list&api_params=%7B%22page%22:1%7D")
    response = session.get("https://stips.co.il/api?name=messages.list")
    response = json.loads(response.content)

    lasted_msg = response["data"]["messages"][0]
    user_chat = lasted_msg["itemProfile"]["userid"]
    from_user = lasted_msg["fromuserid"]

    # print(lasted_msg["msg"])
    # printBlue(f"new_messages: {new_messages}")

    if lasted_msg != new_messages[-1]\
            and from_user == user_chat: # There new message & It's not from you
        new_messages.append(lasted_msg)
        printGreen("You got new message! 🛎")
        print(lasted_msg["msg"])
    # else: printYellow(f"No new messages found yet.")
    # print(new_messages)

    whileIndex += 1
    # if whileIndex == 100:
    #   break
    sleep(5) # 5*60 times = 5 minutes



# region FULL RESPONSE:
# {
#   "status": "ok",
#   "error_code": "",
#   "data": {
#     "messages": [
#       {
#         "id": 260152214,
#         "touserid": 139326,
#         "fromuserid": 169905,
#         "msg": "לא יודעת למה",
#         "fromtokey": 139326000169905,
#         "time": "2021\/05\/14 19:37:37",
#         "viewtime": null,
#         "hebrew_time": "11 דקות",
#         "newCount": 3,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": ".Alaska.",
#           "anonflg": false,
#           "active": true,
#           "userid": 169905,
#           "photostamp": "4787313752854",
#           "online": true
#         }
#       },
#       {
#         "id": 260146735,
#         "touserid": 139326,
#         "fromuserid": 311148,
#         "msg": "BRUH 3",
#         "fromtokey": 139326000311148,
#         "time": "2021\/05\/14 18:33:21",
#         "viewtime": null,
#         "hebrew_time": "שעה",
#         "newCount": 1,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": "yahoo~",
#           "anonflg": false,
#           "active": true,
#           "userid": 311148,
#           "photostamp": "",
#           "online": false
#         }
#       },
#       {
#         "id": 260141653,
#         "touserid": 247180,
#         "fromuserid": 139326,
#         "msg": "מי אוהב את השבת",
#         "fromtokey": 139326000247180,
#         "time": "2021\/05\/14 17:50:43",
#         "viewtime": "14/05/2021 18:20:44",
#         "hebrew_time": "שעה",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "-NiceGirl-",
#           "anonflg": false,
#           "active": true,
#           "userid": 247180,
#           "photostamp": "49104354550853",
#           "online": true
#         }
#       },
#       {
#         "id": 260079609,
#         "touserid": 139326,
#         "fromuserid": 215493,
#         "msg": "באלי גם",
#         "fromtokey": 139326000215493,
#         "time": "2021\/05\/14 01:56:36",
#         "viewtime": null,
#         "hebrew_time": "17 שעות",
#         "newCount": 3,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": "I'm The Real Slim Shady",
#           "anonflg": false,
#           "active": true,
#           "userid": 215493,
#           "photostamp": "46112327548854",
#           "online": false
#         }
#       },
#       {
#         "id": 260078363,
#         "touserid": 139326,
#         "fromuserid": 257533,
#         "msg": "עדיף לאף אחד לא לשמוע :\/",
#         "fromtokey": 139326000257533,
#         "time": "2021\/05\/14 01:47:32",
#         "viewtime": "14/05/2021 01:47:58",
#         "hebrew_time": "18 שעות",
#         "newCount": 0,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": "Nighttcore",
#           "anonflg": false,
#           "active": true,
#           "userid": 257533,
#           "photostamp": "4769357844854",
#           "online": false
#         }
#       },
#       {
#         "id": 260077511,
#         "touserid": 211003,
#         "fromuserid": 139326,
#         "msg": "אגדל כנף למענייךך",
#         "fromtokey": 139326000211003,
#         "time": "2021\/05\/14 01:42:25",
#         "viewtime": null,
#         "hebrew_time": "18 שעות",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "Chiquititia",
#           "anonflg": false,
#           "active": true,
#           "userid": 211003,
#           "photostamp": "4795304552854",
#           "online": false
#         }
#       },
#       {
#         "id": 260070532,
#         "touserid": 280257,
#         "fromuserid": 139326,
#         "msg": "מרגלים",
#         "fromtokey": 139326000280257,
#         "time": "2021\/05\/14 00:58:59",
#         "viewtime": null,
#         "hebrew_time": "18 שעות",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "~Chill~",
#           "anonflg": false,
#           "active": true,
#           "userid": 280257,
#           "photostamp": "4784236339854",
#           "online": false
#         }
#       },
#       {
#         "id": 259969134,
#         "touserid": 249396,
#         "fromuserid": 139326,
#         "msg": "שמעי כפרה ה3 בלילה אני בדרום תל אביב מנסה לא להדקר כולי מחוק לא פנוי לספר לך סיפור לפני שינה",
#         "fromtokey": 139326000249396,
#         "time": "2021\/05\/13 03:05:41",
#         "viewtime": "13/05/2021 16:45:29",
#         "hebrew_time": "13 במאי 2021, 03:05",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "Idc :)",
#           "anonflg": false,
#           "active": true,
#           "userid": 249396,
#           "photostamp": "4374357965854",
#           "online": false
#         }
#       },
#       {
#         "id": 259968792,
#         "touserid": 139326,
#         "fromuserid": 228941,
#         "msg": "עצם זה שהיא אישה גורם לאנשים להגיב",
#         "fromtokey": 139326000228941,
#         "time": "2021\/05\/13 03:03:06",
#         "viewtime": "13/05/2021 03:05:51",
#         "hebrew_time": "13 במאי 2021, 03:03",
#         "newCount": 0,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": "האיש והשפם",
#           "anonflg": false,
#           "active": true,
#           "userid": 228941,
#           "photostamp": "47119147846854",
#           "online": true
#         }
#       },
#       {
#         "id": 259966870,
#         "touserid": 287976,
#         "fromuserid": 139326,
#         "msg": "שזה מדליק",
#         "fromtokey": 139326000287976,
#         "time": "2021\/05\/13 02:47:13",
#         "viewtime": "13/05/2021 02:48:11",
#         "hebrew_time": "13 במאי 2021, 02:47",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "משעמם לי רצח ",
#           "anonflg": false,
#           "active": true,
#           "userid": 287976,
#           "photostamp": "4794286248854",
#           "online": false
#         }
#       },
#       {
#         "id": 259919062,
#         "touserid": 243875,
#         "fromuserid": 139326,
#         "msg": "חחחחח כן",
#         "fromtokey": 139326000243875,
#         "time": "2021\/05\/12 19:58:03",
#         "viewtime": null,
#         "hebrew_time": "12 במאי 2021, 19:58",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "?O K",
#           "anonflg": false,
#           "active": true,
#           "userid": 243875,
#           "photostamp": "47109267752854",
#           "online": false
#         }
#       },
#       {
#         "id": 259894101,
#         "touserid": 275440,
#         "fromuserid": 139326,
#         "msg": "לצערי זה הפך להיות כמו חג, בכל שנה בין מאי (5) לאוגוסט (8). כשבוע ימים של מאפייני החג - חדשות רועמות, הרוגים, פיצוצים בשמיים, בריחה לממדים ואחדות של העם",
#         "fromtokey": 139326000275440,
#         "time": "2021\/05\/12 15:28:15",
#         "viewtime": "12/05/2021 15:29:10",
#         "hebrew_time": "12 במאי 2021, 15:28",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "לא אכפת לי.",
#           "anonflg": false,
#           "active": true,
#           "userid": 275440,
#           "photostamp": "4787297552854",
#           "online": false
#         }
#       },
#       {
#         "id": 259893686,
#         "touserid": 139326,
#         "fromuserid": 288233,
#         "msg": "ץודה רבה",
#         "fromtokey": 139326000288233,
#         "time": "2021\/05\/12 15:22:58",
#         "viewtime": "12/05/2021 15:22:59",
#         "hebrew_time": "12 במאי 2021, 15:22",
#         "newCount": 0,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": "Lea-",
#           "anonflg": false,
#           "active": true,
#           "userid": 288233,
#           "photostamp": "45104224541854",
#           "online": false
#         }
#       },
#       {
#         "id": 259874123,
#         "touserid": 315079,
#         "fromuserid": 139326,
#         "msg": "מיס אם תראי תהודעה הזו, תדעי שמחקתי תסטיפס.\n\nמשתדל להתרכז בדברים שחשובים לי ובהתאם כן הייתי רוצה להמשיך לדבר איתך\n\nמוזמנת לשלוח הודעה מהאינסטה הריק שלך\nidan_biton16\n\nנ.ב יש את זה ביותר דרמטי?",
#         "fromtokey": 139326000315079,
#         "time": "2021\/05\/12 10:20:33",
#         "viewtime": "12/05/2021 10:45:02",
#         "hebrew_time": "12 במאי 2021, 10:20",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "Evaa",
#           "anonflg": false,
#           "active": true,
#           "userid": 315079,
#           "photostamp": "4663352468854",
#           "online": false
#         }
#       },
#       {
#         "id": 259811614,
#         "touserid": 139326,
#         "fromuserid": 209128,
#         "msg": "ביצהה",
#         "fromtokey": 139326000209128,
#         "time": "2021\/05\/11 20:40:12",
#         "viewtime": "11/05/2021 20:40:36",
#         "hebrew_time": "11 במאי 2021, 20:40",
#         "newCount": 0,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": "פרפרים צבעוניים",
#           "anonflg": false,
#           "active": true,
#           "userid": 209128,
#           "photostamp": "5182313259853",
#           "online": false
#         }
#       },
#       {
#         "id": 259739661,
#         "touserid": 139326,
#         "fromuserid": 295654,
#         "msg": "או שכן",
#         "fromtokey": 139326000295654,
#         "time": "2021\/05\/11 01:21:22",
#         "viewtime": "11/05/2021 01:22:27",
#         "hebrew_time": "11 במאי 2021, 01:21",
#         "newCount": 0,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": "Tiger.r",
#           "anonflg": false,
#           "active": true,
#           "userid": 295654,
#           "photostamp": "5464277959853",
#           "online": false
#         }
#       },
#       {
#         "id": 259739175,
#         "touserid": 139326,
#         "fromuserid": 319593,
#         "msg": "לזה בקושי מגיבים גם לבנות",
#         "fromtokey": 139326000319593,
#         "time": "2021\/05\/11 01:17:11",
#         "viewtime": "11/05/2021 01:18:03",
#         "hebrew_time": "11 במאי 2021, 01:17",
#         "newCount": 0,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": "Israeli lives matter",
#           "anonflg": false,
#           "active": true,
#           "userid": 319593,
#           "photostamp": "4787306549854",
#           "online": false
#         }
#       },
#       {
#         "id": 259738743,
#         "touserid": 221734,
#         "fromuserid": 139326,
#         "msg": "בעע",
#         "fromtokey": 139326000221734,
#         "time": "2021\/05\/11 01:12:43",
#         "viewtime": "11/05/2021 01:12:59",
#         "hebrew_time": "11 במאי 2021, 01:12",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "^_^ א(ו)הבת (ל)חייך:-*",
#           "anonflg": false,
#           "active": true,
#           "userid": 221734,
#           "photostamp": "4677146945853",
#           "online": false
#         }
#       },
#       {
#         "id": 259737083,
#         "touserid": 309092,
#         "fromuserid": 139326,
#         "msg": "אפילו אם זה לא את בתמונה, לנו כגברים תמיד יש תקווה",
#         "fromtokey": 139326000309092,
#         "time": "2021\/05\/11 00:59:39",
#         "viewtime": "11/05/2021 01:48:05",
#         "hebrew_time": "11 במאי 2021, 00:59",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "תהיו חברים שלי אמן",
#           "anonflg": false,
#           "active": true,
#           "userid": 309092,
#           "photostamp": "4398204769854",
#           "online": false
#         }
#       },
#       {
#         "id": 259721203,
#         "touserid": 139326,
#         "fromuserid": 241346,
#         "msg": "אני לא יכול להתגיס",
#         "fromtokey": 139326000241346,
#         "time": "2021\/05\/10 23:05:28",
#         "viewtime": "10/05/2021 23:32:16",
#         "hebrew_time": "10 במאי 2021, 23:05",
#         "newCount": 0,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": "Asaf 1",
#           "anonflg": false,
#           "active": true,
#           "userid": 241346,
#           "photostamp": "46113162265854",
#           "online": false
#         }
#       },
#       {
#         "id": 259673776,
#         "touserid": 46501,
#         "fromuserid": 139326,
#         "msg": "אני מתכנת שכן עושים דברים יעילים ומוכר אותם. צור איתי קשר בווטסאפ 0584770076",
#         "fromtokey": 46501000139326,
#         "time": "2021\/05\/10 14:09:17",
#         "viewtime": null,
#         "hebrew_time": "10 במאי 2021, 14:09",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "Spongebob Roundpants",
#           "anonflg": false,
#           "active": true,
#           "userid": 46501,
#           "photostamp": "47121246141854",
#           "online": false
#         }
#       },
#       {
#         "id": 259669022,
#         "touserid": 163220,
#         "fromuserid": 139326,
#         "msg": "שמיניזם כפרה סיימנו ללמוד את באה לי עם העקומות והסטיות של פיתגורס",
#         "fromtokey": 139326000163220,
#         "time": "2021\/05\/10 12:57:38",
#         "viewtime": "10/05/2021 18:45:30",
#         "hebrew_time": "10 במאי 2021, 12:57",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "היפיפייה הנרדמת❤",
#           "anonflg": false,
#           "active": true,
#           "userid": 163220,
#           "photostamp": "53114223068853",
#           "online": false
#         }
#       },
#       {
#         "id": 259645125,
#         "touserid": 260843,
#         "fromuserid": 139326,
#         "msg": "שמעקס",
#         "fromtokey": 139326000260843,
#         "time": "2021\/05\/10 01:14:19",
#         "viewtime": null,
#         "hebrew_time": "10 במאי 2021, 01:14",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": ":)Lee",
#           "anonflg": false,
#           "active": true,
#           "userid": 260843,
#           "photostamp": "47111305852854",
#           "online": true
#         }
#       },
#       {
#         "id": 259606847,
#         "touserid": 139326,
#         "fromuserid": 292449,
#         "msg": "כן זה סבבה כזה",
#         "fromtokey": 139326000292449,
#         "time": "2021\/05\/09 19:53:33",
#         "viewtime": "09/05/2021 19:54:55",
#         "hebrew_time": "9 במאי 2021, 19:53",
#         "newCount": 0,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": "גברך לעתיד  ",
#           "anonflg": false,
#           "active": true,
#           "userid": 292449,
#           "photostamp": "47117246051854",
#           "online": false
#         }
#       },
#       {
#         "id": 259564513,
#         "touserid": 264485,
#         "fromuserid": 139326,
#         "msg": "מוזמן להצטרף לערוץ טלגרם שלי\nHttps:\/\/T.me\/BlackJobs",
#         "fromtokey": 139326000264485,
#         "time": "2021\/05\/09 08:09:30",
#         "viewtime": "09/05/2021 09:01:14",
#         "hebrew_time": "9 במאי 2021, 08:09",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "מה אתם רוציםם",
#           "anonflg": false,
#           "active": true,
#           "userid": 264485,
#           "photostamp": "",
#           "online": false
#         }
#       },
#       {
#         "id": 259523388,
#         "touserid": 139326,
#         "fromuserid": 241905,
#         "msg": "רק בעיות יש שם",
#         "fromtokey": 139326000241905,
#         "time": "2021\/05\/09 00:27:08",
#         "viewtime": "09/05/2021 00:28:04",
#         "hebrew_time": "9 במאי 2021, 00:27",
#         "newCount": 0,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": "     Z",
#           "anonflg": false,
#           "active": true,
#           "userid": 241905,
#           "photostamp": "5073332240853",
#           "online": false
#         }
#       },
#       {
#         "id": 259438896,
#         "touserid": 262578,
#         "fromuserid": 139326,
#         "msg": ":broken_heart:",
#         "fromtokey": 139326000262578,
#         "time": "2021\/05\/08 02:35:05",
#         "viewtime": "08/05/2021 02:39:09",
#         "hebrew_time": "8 במאי 2021, 02:35",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": " Alin ",
#           "anonflg": false,
#           "active": true,
#           "userid": 262578,
#           "photostamp": "47119345845854",
#           "online": false
#         }
#       },
#       {
#         "id": 259430816,
#         "touserid": 252253,
#         "fromuserid": 139326,
#         "msg": "עאזבי",
#         "fromtokey": 139326000252253,
#         "time": "2021\/05\/08 01:03:57",
#         "viewtime": "08/05/2021 01:04:07",
#         "hebrew_time": "8 במאי 2021, 01:03",
#         "newCount": 0,
#         "currentUserMsg": true,
#         "itemProfile": {
#           "nickname": "מחשפנת בזמני הפנוי",
#           "anonflg": false,
#           "active": true,
#           "userid": 252253,
#           "photostamp": "47119295146854",
#           "online": false
#         }
#       },
#       {
#         "id": 259430200,
#         "touserid": 139326,
#         "fromuserid": 55927,
#         "msg": "אז יש לי קצת ידע על מה קורה פה... אם תרצה בשמחה",
#         "fromtokey": 55927000139326,
#         "time": "2021\/05\/08 00:57:59",
#         "viewtime": "08/05/2021 01:02:10",
#         "hebrew_time": "8 במאי 2021, 00:57",
#         "newCount": 0,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": "פעם גולנצ'יק - תמיד גולנצ'יק",
#           "anonflg": false,
#           "active": true,
#           "userid": 55927,
#           "photostamp": "50116133659852",
#           "online": false
#         }
#       },
#       {
#         "id": 259428952,
#         "touserid": 139326,
#         "fromuserid": 288202,
#         "msg": "כמה ימים",
#         "fromtokey": 139326000288202,
#         "time": "2021\/05\/08 00:44:17",
#         "viewtime": "08/05/2021 00:46:20",
#         "hebrew_time": "8 במאי 2021, 00:44",
#         "newCount": 0,
#         "currentUserMsg": false,
#         "itemProfile": {
#           "nickname": "דקסמול קולד",
#           "anonflg": false,
#           "active": true,
#           "userid": 288202,
#           "photostamp": "47110344349854",
#           "online": false
#         }
#       }
#     ]
#   },
#   "sqls": [
#     {
#       "source": "getMessagesList",
#       "exec_time": 0
#     }
#   ],
#   "exec_time": "234ms"
# }
# endregion FULL RESPONSE:



