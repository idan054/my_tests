from bs4 import BeautifulSoup, SoupStrainer
from pprint import pprint
import requests, pickle
import json

## delivery_butik() not works

session = requests.session()
global csrf_token

## Get pre-login cookies & csrf_token
def pre_login_cookies():
    global csrf_token
    response = session.get("https://members.lionwheel.com/?locale=he", data="")
    # pprint(response.status_code)
    # pprint(response.cookies)
    # pprint(response.content)

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
    # pprint(csrf_token)

    _dict = {"csrf_token": csrf_token}
    with open("../config/butik25_config.json", "w") as f:
        json.dump(_dict, f)

        return csrf_token # response.cookies - No need

# get cookies & csrf_token from file / pre_login_cookies()
try:
    with open('../config/pre-login_butik25_Cookies', 'rb') as f:
        session.cookies.update(pickle.load(f))
    pprint("Pre-login cookies from file")
except:
    pre_login_cookies()
    pprint("New pre-login cookies has created")

# Note: if pre-login_butik25_Cookies exist, its mean butik25_config.json exist too
with open('../config/butik25_config.json') as json_file:
    config_file = json.load(json_file)
csrf_token = config_file["csrf_token"]


## Login butik25
def login_butik25():
    payload = {
        # "authenticity_token": "hcDMmb19opECiH2l5a/MZ22RgOAGLL39SoW7klaHyeW1sCiNUWiFrDABgR8B3+c/noTX+BW15pwHcq097BnpEQ==",
        "authenticity_token": csrf_token,
        "user[username]": "ספיידר תלת מימד",
        "user[password]": "0585551234",
        # "user[remember_me]": 0,
        "user[remember_me]": 1
    }

    response = session.post("https://members.lionwheel.com/users/sign_in?locale=he", data=payload)
    pprint(response.status_code)
    # pprint(response.cookies)
    # pprint(response.content)

    #~ Save cookies to file
    # _lionwheel_session cookie
    # remember_user_token cookie
    with open('../config/post-login_butik25_Cookies', 'wb') as f:
        pickle.dump(session.cookies, f)
login_butik25()


# print(len(session.cookies.keys))
session.cookies.clear()
# session.cookies.set("_lionwheel_session", "UQCQBLV7DW7EzpVH0m6TP8vCRgra7WCG88URznk3YJSY0amSeMnEpEkobOU1p1yt4D5YGOco5M6Fp9AB")
# session.cookies.set("remember_user_token", "eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczVNekV3WFN3aUpESmhKREV4SkdKeWFGZGtlbFJzVVVneE5tZHRMMG95VHpSVVYwOGlMQ0l4TmpJd09ESTNOVE14TGpFMk16WXlOemtpWFE9PSIsImV4cCI6IjIwMjItMDUtMTJUMTM6NTI6MTEuMTYzWiIsInB1ciI6ImNvb2tpZS5yZW1lbWJlcl91c2VyX3Rva2VuIn19--9bad43536473bbed10a89b83164eeaf939625e96")
# pprint(session.cookies.get_dict())

session.headers.update({"Cookie": "_gcl_au=1.1.1816081929.1620408946; _hjTLDTest=1; _hjid=8b7264c2-776a-4311-8de5-7cfc0ff76ccd; _fbp=fb.1.1620408946642.729566022; _ga_ZGBQN259MY=GS1.1.1620408945.1.1.1620408976.0; _ga=GA1.2.2091998165.1620408946; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczVNekV3WFN3aUpESmhKREV4SkdKeWFGZGtlbFJzVVVneE5tZHRMMG95VHpSVVYwOGlMQ0l4TmpJd09ESTNOVE14TGpFMk16WXlOemtpWFE9PSIsImV4cCI6IjIwMjItMDUtMTJUMTM6NTI6MTEuMTYzWiIsInB1ciI6ImNvb2tpZS5yZW1lbWJlcl91c2VyX3Rva2VuIn19--9bad43536473bbed10a89b83164eeaf939625e96; _lionwheel_session=UQCQBLV7DW7EzpVH0m6TP8vCRgra7WCG88URznk3YJSY0amSeMnEpEkobOU1p1yt4D5YGOco5M6Fp9AB%2FMBg81flPbfdRgfe2BikxqiDQOumZSez1sZfmLBspg0BslgpbJr5B%2B0z6Wd6LFYK6qosPd4s40VNx7aL%2B%2Ftx1FqDC2LnjmNqJl0ztRtxp%2Bh4FruueYvGhUXmCA1lEnL3%2FqfJQtX8acuXlQ%2Bghzkg2nV4nHyuyR0tkC9MiPFwWw7ssouGQ2bjDu0hIfH9cySGUzpTpl19yfqWUPiHnxANzPw3whxrGWHEv0ziRUx4shAuFhe1wEhXRPcnaDcUgG%2F5A051iRCTBseuRjylgij2ISmYyaftuMHIN8AueqvxHA18Heh0y%2FZS%2FQEUAO4slz9wNnla1LAgETU%2BnIvMAgUNfDWtiNsNbw%3D%3D--hcTV8oezlRezbQEs--Ob%2BBinxZgcKxiMHneb84jA%3D%3D; _gid=GA1.2.1106100520.1621335698; _gat_gtag_UA_122455023_2=1"})
pprint(session.headers)

# pprint(session.cookies.values)
## Create delivery butik25
def delivery_butik25():
    payload = {
        "authenticity_token": csrf_token,
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


    response = session.post("https://members.lionwheel.com/tasks?locale=he" # &authenticity_token=w8NbSeD2najEyICgzcmpV4ItwNpu8zfsWhDgFsQtwuqhC2XhkrHoUgFK6IUUjROfHDq57z9EiMP1sqcAzQL6Fw%3D%3D&task%5Btiming_type%5D=timingNow&task%5Btask_date%5D=18%2F05%2F2021&task%5Bfixed_start_date%5D=&task%5Bfixed_end_date%5D=31%2F12%2F2030&fixed_appear_time=6%3A00&task%5Bis_sunday%5D=0&task%5Bis_monday%5D=0&task%5Bis_tuesday%5D=0&task%5Bis_wednesday%5D=0&task%5Bis_thursday%5D=0&task%5Bis_friday%5D=0&task%5Bis_saturday%5D=0&task%5Burgency%5D=REGULAR&task%5Bpackages_quantity%5D=1&task%5Bsource_location%5D=&task%5Bsource_name%5D=&task%5Bsource_city%5D=&task%5Bsource_city_other%5D=&task%5Bsource_street%5D=&task%5Bsource_street_other%5D=&task%5Bsource_zone%5D=&task%5Bsource_number%5D=&task%5Bsource_floor%5D=&task%5Bsource_apartment%5D=&task%5Bsource_notes%5D=&task%5Bsource_recipient_name%5D=&task%5Bsource_phone%5D=&task%5Bsource_email%5D=&task%5Bsave_source_location%5D=0&task%5Bdestination_location%5D=76201&task%5Bdestination_name%5D=%D7%A1%D7%A4%D7%99%D7%99%D7%93%D7%A8+%D7%AA%D7%9C%D7%AA+%D7%9E%D7%99%D7%9E%D7%93&task%5Bdestination_city_other%5D=%D7%92%D7%93%D7%A8%D7%94&task%5Bdestination_street_other%5D=%D7%97%D7%91%D7%A7%D7%95%D7%A7&task%5Bdestination_zone%5D=&task%5Bdestination_number%5D=114&task%5Bdestination_floor%5D=&task%5Bdestination_apartment%5D=&task%5Bdestination_notes%5D=&task%5Bdestination_recipient_name%5D=%D7%90%D7%A4%D7%A8%D7%AA&task%5Bdestination_phone%5D=0542323167&task%5Bdestination_email%5D=info%40spider3d.co.il%E2%80%8F&task%5Bsave_destination_location%5D=0&task%5Bnotes%5D=&button="
                            # , data=payload
                            )
    pprint(response.status_code)
    # pprint(response.cookies)
    # pprint(response.content)

    # Save cookies to file
    # # _lionwheel_session cookie
    # # remember_user_token cookie
    # with open('../config/post-login_butik25_Cookies', 'wb') as f:
    #     pickle.dump(session.cookies, f)
delivery_butik25()




