from bs4 import BeautifulSoup, SoupStrainer
import requests, pickle
import json

## delivery_butik() not works

session = requests.session()
global csrf_token

## Get pre-login cookies & csrf_token
def pre_login_cookies():
    global csrf_token
    response = session.get("https://members.lionwheel.com/?locale=he", data="")
    # print(response.status_code)
    # print(response.cookies)
    # print(response.content)

    #~ Save cookies to file
    # _lionwheel_session cookie
    with open('../config/pre-login_butik25_Cookies', 'wb') as f:
        pickle.dump(session.cookies, f)

    for element in BeautifulSoup(response.content,
                              # Element type like body, class..
                              parse_only=SoupStrainer('meta'),
                              features="html.parser"):
        # Attribute type (line) like </a>, </script>
        if element.has_attr("name") \
            and len(element["content"]) == 88:
            # Value in line like like href=, name=
            csrf_token = element["content"]
            break
    # print(csrf_token)

    _dict = {"csrf_token": csrf_token}
    with open("../config/butik25_config.json", "w") as f:
        json.dump(_dict, f)

        return csrf_token # response.cookies - No need

# get cookies & csrf_token from file / pre_login_cookies()
try:
    with open('../config/pre-login_butik25_Cookies', 'rb') as f:
        session.cookies.update(pickle.load(f))
    print("Pre-login cookies from file")
except:
    pre_login_cookies()
    print("New pre-login cookies has created")

# Note: if pre-login_butik25_Cookies exist, its mean butik25_config.json exist too
with open('../config/butik25_config.json') as json_file:
    config_file = json.load(json_file)
csrf_token = config_file["csrf_token"]


## Login butik25

def login_butik25():
    payload = {
        # "authenticity_token": "hcDMmb19opECiH2l5a/MZ22RgOAGLL39SoW7klaHyeW1sCiNUWiFrDABgR8B3+c/noTX+BW15pwHcq097BnpEQ==",
        "authenticity_token": csrf_token,
        # "user[username]": "ספיידר תלת מימד",
        # "user[password]": "0585551234",
        # "user[remember_me]": 0,
        "user[remember_me]": 1
    }

    response = session.post("https://members.lionwheel.com/users/sign_in?locale=he", data=payload)
    print(response.status_code)
    # print(response.cookies)
    # print(response.content)

    #~ Save cookies to file
    # _lionwheel_session cookie
    # remember_user_token cookie
    with open('../config/post-login_butik25_Cookies', 'wb') as f:
        pickle.dump(session.cookies, f)
login_butik25()


print(session.cookies)
## Create delivery butik25
def delivery_butik25():
    payload = {
        "authenticity_token": csrf_token,
        "user[username]": "ספיידר תלת מימד",
        "user[password]": "0585551234",
        "task":{
        "timing_type": "timingNow",
        "task_date": "15/05/2021",
        "fixed_start_date": "",
        "fixed_end_date": "31/12/2030",
        "is_sunday": "0",
        "is_monday": "0",
        "is_tuesday": "0",
        "is_wednesday": "0",
        "is_thursday": "0",
        "is_friday": "0",
        "is_saturday": "0",
        "urgency": "REGULAR",
        "packages_quantity": "1",
        "source_location": "76201",
        "source_name": "ספיידר תלת מימד",
        "source_city_other": "גדרה",
        "source_street_other": "חבקוק",
        "source_zone": "",
        "source_number": "114",
        "source_floor": "",
        "source_apartment": "",
        "source_notes": "",
        "source_recipient_name": "אפרת",
        "source_phone": "0542323167",
        "source_email": "info@spider3d.co.il‏",
        "save_source_location": "0",
        "destination_location": "",
        "destination_name": "ישראל ישראלי",
        "destination_city": "תל אביב - יפו",
        "destination_city_other": "",
        "destination_street": "ויצמן",
        "destination_street_other": "",
        "destination_zone": "",
        "destination_number": "90",
        "destination_floor": "",
        "destination_apartment": "",
        "destination_notes": "משלוח בקשת בדיקה",
        "destination_recipient_name": "",
        "destination_phone": "0584770076",
        "destination_email": "idanbit80@gmail.com",
        "save_destination_location": "0",
        "notes": "pickup-note הערת משלוח",
    },
        "fixed_appear_time": "6:00",
        "button": ""
    }

    response = session.get("https://members.lionwheel.com/tasks?locale=he"
                            # , data=payload
                            )
    print(response.status_code)
    # print(response.cookies)
    # print(response.content)

    response = session.post("https://members.lionwheel.com/tasks?locale=he"
                            , data=payload
                            )
    print(response.status_code)
    print(response.cookies)
    print(response.content)

    # Save cookies to file
    # # _lionwheel_session cookie
    # # remember_user_token cookie
    # with open('../config/post-login_butik25_Cookies', 'wb') as f:
    #     pickle.dump(session.cookies, f)

delivery_butik25()




