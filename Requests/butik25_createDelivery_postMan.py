from bs4 import BeautifulSoup, SoupStrainer
from pprint import pprint
import requests, pickle
import json

## delivery_butik() not works

session = requests.session()
LOGIN_USER = "ספיידר תלת מימד"
LOGIN_PASS = "0585551234"
# LOGIN_USER = "טופ"
# LOGIN_PASS = "059947"
global csrf_token
global _csrf_token # Create delivery


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
        f.write("\n// csrf_token is not a cookie!")

        return csrf_token # response.cookies - No need

# get cookies from pre-login cookie file / pre_login_cookies()
try:
    with open('../config/pre-login_butik25_Cookies', 'rb') as f:
        session.cookies.update(pickle.load(f))
    pprint("Pre-login cookies from file")
except:
    pre_login_cookies()
    pprint("New pre-login cookies has created")

# Note: if pre-login_butik25_Cookies exist, its mean butik25_config.json exist too
# set csrf_token value
with open('../config/butik25_config.json') as json_file:
    config_file = json.load(json_file)
csrf_token = config_file["csrf_token"]


## Login butik25
def login_butik25():
    payload = {
        # "authenticity_token": "hcDMmb19opECiH2l5a/MZ22RgOAGLL39SoW7klaHyeW1sCiNUWiFrDABgR8B3+c/noTX+BW15pwHcq097BnpEQ==",
        "authenticity_token": csrf_token,
        "user[username]": LOGIN_USER,
        "user[password]": LOGIN_PASS,
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

_cookies = session.cookies.values()
# session.cookies.clear()
# session.headers.update({"Cookie": "_gcl_au=1.1.1816081929.1620408946; _hjTLDTest=1; _hjid=8b7264c2-776a-4311-8de5-7cfc0ff76ccd; _fbp=fb.1.1620408946642.729566022; _ga_ZGBQN259MY=GS1.1.1620408945.1.1.1620408976.0; _ga=GA1.2.2091998165.1620408946; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczVNekV3WFN3aUpESmhKREV4SkdKeWFGZGtlbFJzVVVneE5tZHRMMG95VHpSVVYwOGlMQ0l4TmpJd09ESTNOVE14TGpFMk16WXlOemtpWFE9PSIsImV4cCI6IjIwMjItMDUtMTJUMTM6NTI6MTEuMTYzWiIsInB1ciI6ImNvb2tpZS5yZW1lbWJlcl91c2VyX3Rva2VuIn19--9bad43536473bbed10a89b83164eeaf939625e96; _lionwheel_session=UQCQBLV7DW7EzpVH0m6TP8vCRgra7WCG88URznk3YJSY0amSeMnEpEkobOU1p1yt4D5YGOco5M6Fp9AB%2FMBg81flPbfdRgfe2BikxqiDQOumZSez1sZfmLBspg0BslgpbJr5B%2B0z6Wd6LFYK6qosPd4s40VNx7aL%2B%2Ftx1FqDC2LnjmNqJl0ztRtxp%2Bh4FruueYvGhUXmCA1lEnL3%2FqfJQtX8acuXlQ%2Bghzkg2nV4nHyuyR0tkC9MiPFwWw7ssouGQ2bjDu0hIfH9cySGUzpTpl19yfqWUPiHnxANzPw3whxrGWHEv0ziRUx4shAuFhe1wEhXRPcnaDcUgG%2F5A051iRCTBseuRjylgij2ISmYyaftuMHIN8AueqvxHA18Heh0y%2FZS%2FQEUAO4slz9wNnla1LAgETU%2BnIvMAgUNfDWtiNsNbw%3D%3D--hcTV8oezlRezbQEs--Ob%2BBinxZgcKxiMHneb84jA%3D%3D; _gid=GA1.2.1106100520.1621335698; _gat_gtag_UA_122455023_2=1"})
# session.headers.update({'Cookie': f'_lionwheel_session={_cookies[0]}; remember_user_token={_cookies[1]}'})
# print(_cookies)

session.headers.update({'Cookie': f'_lionwheel_session={_cookies[0]}; remember_user_token={_cookies[1]}'})
# print(session.headers)

## GET CSRF_TOKEN for delivery
url = "https://members.lionwheel.com/tasks/new?locale=he"

# headers = { # 'Cookie': '_lionwheel_session=FR04oUWmig%2BXUR7C6STXT3RN5G5%2Fnr5G6GQYdGRv3Nu%2Fr3YheZc5z1Co3Q0s5sLszbMOyNKaEiu%2FncXPK%2Bx9aGIrpzj0PsioxBYe3pz9mVDJUw1uOm%2BHYpU1jlVIAZ1KhCtpo5eJoWykbOF6iP%2FUMxqHuI4roCO0ED%2FNIU6WJjhtkOow6NSqrMLs9%2FxuD1U0taJVQQ9pQAjIuofUzr%2FX7jrRh0d6JGutX6jazwHTzCYMLz0QNpbqrNxGUblGXM63215ObjFVIGO3N%2BgM0Az3ncmmne0Kmfr2BeqUiiHuW7SiCnjwvkgTh0ttb6oY5PwBp3jyDFEO0aN3VgsGBKYH2VjmqD41NLo2xYJ07YJoyNXS6dGQEwYThBL9Sm3cWPV2k6p7ivUHbk%2FiSIN8cBavF0d1S4HgC%2B2pydQ0KVseIKO9oQ%3D%3D--HGw0tSQBWBpVxUhA--6eCobNqhmxdBDNMOTRQsJw%3D%3D; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczVNekV3WFN3aUpESmhKREV4SkdKeWFGZGtlbFJzVVVneE5tZHRMMG95VHpSVVYwOGlMQ0l4TmpJeU56TXdORGM0TGpJNE5qSTVPQ0pkIiwiZXhwIjoiMjAyMi0wNi0wM1QxNDoyNzo1OC4yODZaIiwicHVyIjoiY29va2llLnJlbWVtYmVyX3VzZXJfdG9rZW4ifX0%3D--748adf168d6c18f7b0b4451fd71042c1055b66df' }

response = session.request("GET", url,
                           # headers=headers, # No Need, already in session
                           )

print(response.status_code)
print(response.text)

for element in BeautifulSoup(response.content,
                             # Element type like body, class..
                             parse_only=SoupStrainer('meta'),
                             features="html.parser"):
    # Attribute type (line) like </a>, </script>
    if element.has_attr("name") \
            and len(element["content"]) == 88:
        # Value in line like like href=, name=
        _csrf_token = element["content"]
        break
    else:
        _csrf_token = "_csrf_token Not Fount"
pprint(_csrf_token)

# create_delivery_csrf_token = get_csrf()

session.headers.clear()
print(session.headers)
## POST DELIVERY
url = "https://members.lionwheel.com/tasks?locale=he"

# payload=f'authenticity_token=YqDdHbwF%2Ftc8hgsCOwP3ppJRQGCu62SFEwIUxIfD1n0pRek4tVxXqMrKm3JsTG7AXQ9qL7LTsMqxJTuY8RPD9g%3D%3D' \
payload=f'authenticity_token={_csrf_token}' \
        '&button=&fixed_appear_time=6%3A00&task%5Bdestination_apartment%5D=&task%5Bdestination_city_other%5D=%D7%92%D7%93%D7%A8%D7%94&task%5Bdestination_email%5D=info%40spider3d.co.il%E2%80%8F&task%5Bdestination_floor%5D=&task%5Bdestination_location%5D=76201&task%5Bdestination_name%5D=%D7%A1%D7%A4%D7%99%D7%99%D7%93%D7%A8%20%D7%AA%D7%9C%D7%AA%20%D7%9E%D7%99%D7%9E%D7%93&task%5Bdestination_notes%5D=&task%5Bdestination_number%5D=114&task%5Bdestination_phone%5D=0542323167&task%5Bdestination_recipient_name%5D=%D7%90%D7%A4%D7%A8%D7%AA&task%5Bdestination_street_other%5D=%D7%97%D7%91%D7%A7%D7%95%D7%A7&task%5Bdestination_zone%5D=&task%5Bfixed_end_date%5D=31%2F12%2F2030&task%5Bfixed_start_date%5D=&task%5Bis_friday%5D=0&task%5Bis_monday%5D=0&task%5Bis_saturday%5D=0&task%5Bis_sunday%5D=0&task%5Bis_thursday%5D=0&task%5Bis_tuesday%5D=0&task%5Bis_wednesday%5D=0&task%5Bnotes%5D=&task%5Bpackages_quantity%5D=1&task%5Bsave_destination_location%5D=0&task%5Bsave_source_location%5D=0&task%5Bsource_apartment%5D=&task%5Bsource_city%5D=&task%5Bsource_city_other%5D=&task%5Bsource_email%5D=&task%5Bsource_floor%5D=&task%5Bsource_location%5D=&task%5Bsource_name%5D=&task%5Bsource_notes%5D=&task%5Bsource_number%5D=&task%5Bsource_phone%5D=&task%5Bsource_recipient_name%5D=&task%5Bsource_street%5D=&task%5Bsource_street_other%5D=&task%5Bsource_zone%5D=&task%5Btask_date%5D=03%2F06%2F2021&task%5Btiming_type%5D=timingNow&task%5Burgency%5D=REGULAR'

headers = {
  # 'Cookie': f'_lionwheel_session={_cookies[0]}; remember_user_token={_cookies[1]}'
  'Cookie': '_lionwheel_session=p4QHByOsbixuNIiQaUL1lPjvnt%2BkzGhCE7kTpwLTuIJfVXRHSFTkZffRG4pk%2BVDg%2FYPZAsGLkzxuR%2BJG%2Bc437S3oNQu6%2BO5gqnQP6mEhbs7CO5M8wAo6EMKN4fnhNAM2HaHUWnzI15IARWouJxSSfoRzCHPiQxNivBTujNqg2Fl6dMJ5j%2BZFew8MOWKQ%2Bw%2FQidB0kA6B5kYjVuVRaNufwKXcy7WsGwTrJ4cSq%2B9YyaxZKA0Wj9iHVuYm4QuFlYDS6VFNotDCPs2KXnPd%2BcFvPf2NXQNNCRoKRgiQkAe7IUYjDxfBRpO0EbFC9FWk7rpvM%2B85%2BtGIw1M%2B%2Biz8UFgbk2qi5uw7f%2BPQMi95idyi9yj393%2BYpfMxaj8iwEyzi3E1iO5C9e8pZ8OY%2F9K8bYkCMj2N2irVDYpL3IwuIeOVvwu6RQ%3D%3D--tfpKkhGg4W5c62SM--6%2B1h%2Bzke7IWWXaWxhjDRNw%3D%3D; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczVNekV3WFN3aUpESmhKREV4SkdKeWFGZGtlbFJzVVVneE5tZHRMMG95VHpSVVYwOGlMQ0l4TmpJeU56STRNak01TGpjNE5Ea3dPRE1pWFE9PSIsImV4cCI6IjIwMjItMDYtMDNUMTM6NTA6MzkuNzg0WiIsInB1ciI6ImNvb2tpZS5yZW1lbWJlcl91c2VyX3Rva2VuIn19--7994c1960bd9e61ea0793558294235001f6f9a4c'
}

response = session.post(url,
                        headers=headers, # No Need, already in session
                        data=payload)
print(response.status_code)
