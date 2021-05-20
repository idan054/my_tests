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


# with open('config/post-login_butik25_Cookies', 'rb') as f:
#     x = pickle.load(f)
#     pprint(x)
# _cookie = x.values()

session.cookies.clear()
_cookies = session.cookies.values()
# session.headers.update({"Cookie": "_gcl_au=1.1.1816081929.1620408946; _hjTLDTest=1; _hjid=8b7264c2-776a-4311-8de5-7cfc0ff76ccd; _fbp=fb.1.1620408946642.729566022; _ga_ZGBQN259MY=GS1.1.1620408945.1.1.1620408976.0; _ga=GA1.2.2091998165.1620408946; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczVNekV3WFN3aUpESmhKREV4SkdKeWFGZGtlbFJzVVVneE5tZHRMMG95VHpSVVYwOGlMQ0l4TmpJd09ESTNOVE14TGpFMk16WXlOemtpWFE9PSIsImV4cCI6IjIwMjItMDUtMTJUMTM6NTI6MTEuMTYzWiIsInB1ciI6ImNvb2tpZS5yZW1lbWJlcl91c2VyX3Rva2VuIn19--9bad43536473bbed10a89b83164eeaf939625e96; _lionwheel_session=UQCQBLV7DW7EzpVH0m6TP8vCRgra7WCG88URznk3YJSY0amSeMnEpEkobOU1p1yt4D5YGOco5M6Fp9AB%2FMBg81flPbfdRgfe2BikxqiDQOumZSez1sZfmLBspg0BslgpbJr5B%2B0z6Wd6LFYK6qosPd4s40VNx7aL%2B%2Ftx1FqDC2LnjmNqJl0ztRtxp%2Bh4FruueYvGhUXmCA1lEnL3%2FqfJQtX8acuXlQ%2Bghzkg2nV4nHyuyR0tkC9MiPFwWw7ssouGQ2bjDu0hIfH9cySGUzpTpl19yfqWUPiHnxANzPw3whxrGWHEv0ziRUx4shAuFhe1wEhXRPcnaDcUgG%2F5A051iRCTBseuRjylgij2ISmYyaftuMHIN8AueqvxHA18Heh0y%2FZS%2FQEUAO4slz9wNnla1LAgETU%2BnIvMAgUNfDWtiNsNbw%3D%3D--hcTV8oezlRezbQEs--Ob%2BBinxZgcKxiMHneb84jA%3D%3D; _gid=GA1.2.1106100520.1621335698; _gat_gtag_UA_122455023_2=1"})
pprint(session.headers.update({'Cookie': '_lionwheel_session=99GXfVQ8o7rux9gxA4dUhTTHvqfBbhnkvCBFR7hV%2BEDc5A9s%2B7Sp26AxWqMHJkXF3prWyu3C1FjvmsnIlsaZOCBUyxhQSX%2B%2Fq8NXSlol11gUEXBugY6%2F9Fp7XCDvw5OjtGIfkcesg2GOqrAnLeQwpeWVERv99tTS%2Fsn44hhgV8nhGfHYcBMom%2Bx4gQC95LeEJJN19TqMWNzkVfbWqNfg4cGHLd2VvKlY%2F1hSOGmaGfM9bbXK1L7l%2Bav%2B0ZkR95sohZsjQLLrIi3E1bSom0K3zTrdKxq6IKBeA6CaVxdosabvr6SJJZ4OI3NXA0jZXyXAfnYqT6u5UbIRHHlUTEnBAqp25kouQF40TpHvFcGe%2F9f%2FB1h581%2FJUBGKqub6GTFOfZE3k0asyu0rfjb1HM4seU%2BXThu8lcPNGyXXzJCFi5zfPg%3D%3D--L49wRb%2BMCLdQxbc4--QrcdXUMc6jLMpP7zje0tMQ%3D%3D; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczBPVGMyWFN3aUpESmhKREV4SkRFME0xTlFkamxMVkRScGVGbFZSVkJLZEhrMldYVWlMQ0l4TmpJeE16TTRNRGMwTGpZME16WTJPVFlpWFE9PSIsImV4cCI6IjIwMjItMDUtMThUMTE6NDE6MTQuNjQzWiIsInB1ciI6ImNvb2tpZS5yZW1lbWJlcl91c2VyX3Rva2VuIn19--b82f8c93dbe9af6f64aa2dd714f4871289587e28'}))


## Create delivery butik25
def create_delivery():
  url = "https://members.lionwheel.com/tasks?locale=he"

  # payload='authenticity_token=FYtw%2BU4FmFD0WN566na6lOMI8Cd%2BcTqFZSmrSCZ6Mqpy7sUJkMXnTFbYuuztVxaR3wiuKoXQPCQ%2FxrJQGuQYdg%3D%3D&button=&fixed_appear_time=6%3A00&task%5Bdestination_apartment%5D=&task%5Bdestination_city_other%5D=%D7%92%D7%93%D7%A8%D7%94&task%5Bdestination_email%5D=info%40spider3d.co.il&task%5Bdestination_floor%5D=&task%5Bdestination_location%5D=33787&task%5Bdestination_name%5D=%D7%A1%D7%A4%D7%99%D7%99%D7%93%D7%A8%20%D7%AA%D7%9C%D7%AA%20%D7%9E%D7%99%D7%9E%D7%93&task%5Bdestination_notes%5D=%D7%90%D7%99%D7%99%D7%9C%20-%20058-5551234&task%5Bdestination_number%5D=114&task%5Bdestination_phone%5D=0522509900&task%5Bdestination_recipient_name%5D=%D7%90%D7%A4%D7%A8%D7%AA%2F%D7%90%D7%99%D7%99%D7%9C&task%5Bdestination_street_other%5D=%D7%97%D7%91%D7%A7%D7%95%D7%A7&task%5Bdestination_zone%5D=&task%5Bdocument_number%5D=&task%5Bfixed_end_date%5D=31%2F12%2F2030&task%5Bfixed_start_date%5D=&task%5Bis_friday%5D=0&task%5Bis_monday%5D=0&task%5Bis_roundtrip%5D=0&task%5Bis_saturday%5D=0&task%5Bis_sunday%5D=0&task%5Bis_thursday%5D=0&task%5Bis_tuesday%5D=0&task%5Bis_wednesday%5D=0&task%5Bmoney_collect%5D=&task%5Bnotes%5D=&task%5Bpackages_quantity%5D=1&task%5Bsame_day%5D=0&task%5Bsave_destination_location%5D=0&task%5Bsave_source_location%5D=0&task%5Bsource_apartment%5D=&task%5Bsource_city%5D=&task%5Bsource_city_other%5D=&task%5Bsource_email%5D=&task%5Bsource_floor%5D=&task%5Bsource_location%5D=&task%5Bsource_name%5D=&task%5Bsource_notes%5D=&task%5Bsource_number%5D=&task%5Bsource_phone%5D=&task%5Bsource_recipient_name%5D=&task%5Bsource_street%5D=&task%5Bsource_street_other%5D=&task%5Bsource_zone%5D=&task%5Bsurfaces_quantity%5D=&task%5Btask_date%5D=18%2F05%2F2021&task%5Btiming_type%5D=timingNow&task%5Burgency%5D=REGULAR&task%5Bvehicle_kind%5D=SCOOTER'

  import json
  payload = {
    'authenticity_token': 'FYtw+U4FmFD0WN566na6lOMI8Cd+cTqFZSmrSCZ6Mqpy7sUJkMXnTFbYuuztVxaR3wiuKoXQPCQ/xrJQGuQYdg==',
    'button': '',
    'fixed_appear_time': '6: 00',
    'task': {
      'destination_apartment': '',
      'destination_city_other': 'גדרה',
      'destination_email': 'info@spider3d.co.il',
      'destination_floor': '',
      'destination_location': '33787',
      'destination_name': 'ספיידרתלתמימד',
      'destination_notes': 'אייל-058-5551234',
      'destination_number': '114',
      'destination_phone': '0522509900',
      'destination_recipient_name': 'אפרת/אייל',
      'destination_street_other': 'חבקוק',
      'destination_zone': '',
      'document_number': '',
      'fixed_end_date': '31/12/2030',
      'fixed_start_date': '',
      'is_friday': '0',
      'is_monday': '0',
      'is_roundtrip': '0',
      'is_saturday': '0',
      'is_sunday': '0',
      'is_thursday': '0',
      'is_tuesday': '0',
      'is_wednesday': '0',
      'money_collect': '',
      'notes': '',
      'packages_quantity': '1',
      'same_day': '0',
      'save_destination_location': '0',
      'save_source_location': '0',
      'source_apartment': '',
      'source_city': '',
      'source_city_other': '',
      'source_email': '',
      'source_floor': '',
      'source_location': '',
      'source_name': '',
      'source_notes': '',
      'source_number': '',
      'source_phone': '',
      'source_recipient_name': '',
      'source_street': '',
      'source_street_other': '',
      'source_zone': '',
      'surfaces_quantity': '',
      'task_date': '18/05/2021',
      'timing_type': 'timingNow',
      'urgency': 'REGULAR',
      'vehicle_kind': 'SCOOTER'
    }
  }
  # payload = json.dumps(payload)

  from querystring_parser import builder as qsbuilder
  payload = qsbuilder.build(payload)  # .replace("[", "%5B").replace("]", "%5D")

  headers = {
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Cookie': '_lionwheel_session=99GXfVQ8o7rux9gxA4dUhTTHvqfBbhnkvCBFR7hV%2BEDc5A9s%2B7Sp26AxWqMHJkXF3prWyu3C1FjvmsnIlsaZOCBUyxhQSX%2B%2Fq8NXSlol11gUEXBugY6%2F9Fp7XCDvw5OjtGIfkcesg2GOqrAnLeQwpeWVERv99tTS%2Fsn44hhgV8nhGfHYcBMom%2Bx4gQC95LeEJJN19TqMWNzkVfbWqNfg4cGHLd2VvKlY%2F1hSOGmaGfM9bbXK1L7l%2Bav%2B0ZkR95sohZsjQLLrIi3E1bSom0K3zTrdKxq6IKBeA6CaVxdosabvr6SJJZ4OI3NXA0jZXyXAfnYqT6u5UbIRHHlUTEnBAqp25kouQF40TpHvFcGe%2F9f%2FB1h581%2FJUBGKqub6GTFOfZE3k0asyu0rfjb1HM4seU%2BXThu8lcPNGyXXzJCFi5zfPg%3D%3D--L49wRb%2BMCLdQxbc4--QrcdXUMc6jLMpP7zje0tMQ%3D%3D; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczBPVGMyWFN3aUpESmhKREV4SkRFME0xTlFkamxMVkRScGVGbFZSVkJLZEhrMldYVWlMQ0l4TmpJeE16TTRNRGMwTGpZME16WTJPVFlpWFE9PSIsImV4cCI6IjIwMjItMDUtMThUMTE6NDE6MTQuNjQzWiIsInB1ciI6ImNvb2tpZS5yZW1lbWJlcl91c2VyX3Rva2VuIn19--b82f8c93dbe9af6f64aa2dd714f4871289587e28'
  }

  response = session.post(url,
                           headers=headers,
                           data=payload)

  # print("response.text Has been copied to clipboard")
  # pyperclip.copy(response.text)
  if response.status_code == 200:
    print("Delivery has been created successfully")
  else:
      print(response.status_code)
  # print(response.request.headers)
create_delivery()





