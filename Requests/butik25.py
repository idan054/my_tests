from time import sleep

from bs4 import BeautifulSoup, SoupStrainer
from pprint import pprint
import requests, pickle
import json
import os
import shutil

## main_delivery()

def main_delivery():
    try: os.mkdir('../config')  # create empty dir
    except: pass

    session = requests.session()
    LOGIN_USER = "ספיידר-3d"
    LOGIN_PASS = "575968"
    TYPE = "Spider-MahirLi"

    # LOGIN_USER = "ספיידר תלת מימד"
    # LOGIN_PASS = "0585551234"
    # TYPE = "Spider-Butik"

    # LOGIN_USER = "טופ"
    # LOGIN_PASS = "059947"
    # TYPE = "Topirzul-Butik"


    ## Get pre-login cookies & csrf_token
    def get_csrf_and_cookies(url, current_type):
        global csrf_token
        response = session.get(url=url, data="")
        # pprint(response._status_code)
        # pprint(response.cookies)
        # pprint(response.content)

        #~ Save cookies to file
        # _lionwheel_session cookie
        with open(f'../config/{current_type}_{TYPE}_Cookies', 'wb') as f:
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
        with open(f"../config/{current_type}_{TYPE}_csrf.json", "w") as f:
            json.dump(_dict, f)

            return csrf_token # response.cookies - No need

    # get cookies from pre-login cookie file / pre_login_cookies()
    def set_csrf_and_cookies(cookieFile, jsonFile, url, _type):
        try:
            # get_csrf_and_cookies(url)

            with open(cookieFile, 'rb') as f:
                session.cookies.update(pickle.load(f))

            with open(jsonFile) as json_file:
                config_file = json.load(json_file)
                # print(config_file)
                csrfToken = config_file["csrf_token"]

            # print(csrfToken)
            # print(session.cookies)
            pprint(f"{_type} cookies and csrf from file")

        except:
            # Cookies auto embed While running this func
            csrfToken = get_csrf_and_cookies(url, _type)
            pprint(f"New {_type} cookies has created")
        return csrfToken

    csrf_token = set_csrf_and_cookies(
                        _type="pre-login",
                         cookieFile=f'../config/pre-login_{TYPE}_Cookies',
                         jsonFile=f'../config/pre-login_{TYPE}_csrf.json',
                         url="https://members.lionwheel.com/?locale=he")
    # print(csrf_token)
    # print()
    # print(session.cookies)

    # print(_cookies)
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

        url  = "https://members.lionwheel.com/users/sign_in?locale=he"

        response = session.post(url=url,
                                # headers=headers, # No Need, already in session
                                data=payload)

        pprint(response.status_code)
        # pprint(response.cookies)
        # pprint(response.content)

        #~ Save cookies to file
        # _lionwheel_session cookie
        # remember_user_token cookie
        with open(f'../config/post-login_{TYPE}_Cookies', 'wb') as f:
            pickle.dump(session.cookies, f)

        ## Get CSRF
        for element in BeautifulSoup(response.content,
                                  # Element type like body, class..
                                  parse_only=SoupStrainer('meta'),
                                  features="html.parser"):
            # Attribute type (line) like </a>, </script>
            if element.has_attr("name") \
                and len(element["content"]) == 88:
                # Value in line like like href=, name=
                current_csrf_token = element["content"]
                break
            else:
                current_csrf_token = "CSRF NOT FOUND"

        return current_csrf_token

    # create_delivery_csrf_token = login_butik25()
    login_butik25()

    # print("create_delivery_csrf_token")
    # pprint(create_delivery_csrf_token)
    # print()
    # print("NEW post login cookies!")
    # print(session.cookies)
    # print(_cookies)
    # session.cookies.clear()
    # session.headers.update({"Cookie": "_gcl_au=1.1.1816081929.1620408946; _hjTLDTest=1; _hjid=8b7264c2-776a-4311-8de5-7cfc0ff76ccd; _fbp=fb.1.1620408946642.729566022; _ga_ZGBQN259MY=GS1.1.1620408945.1.1.1620408976.0; _ga=GA1.2.2091998165.1620408946; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczVNekV3WFN3aUpESmhKREV4SkdKeWFGZGtlbFJzVVVneE5tZHRMMG95VHpSVVYwOGlMQ0l4TmpJd09ESTNOVE14TGpFMk16WXlOemtpWFE9PSIsImV4cCI6IjIwMjItMDUtMTJUMTM6NTI6MTEuMTYzWiIsInB1ciI6ImNvb2tpZS5yZW1lbWJlcl91c2VyX3Rva2VuIn19--9bad43536473bbed10a89b83164eeaf939625e96; _lionwheel_session=UQCQBLV7DW7EzpVH0m6TP8vCRgra7WCG88URznk3YJSY0amSeMnEpEkobOU1p1yt4D5YGOco5M6Fp9AB%2FMBg81flPbfdRgfe2BikxqiDQOumZSez1sZfmLBspg0BslgpbJr5B%2B0z6Wd6LFYK6qosPd4s40VNx7aL%2B%2Ftx1FqDC2LnjmNqJl0ztRtxp%2Bh4FruueYvGhUXmCA1lEnL3%2FqfJQtX8acuXlQ%2Bghzkg2nV4nHyuyR0tkC9MiPFwWw7ssouGQ2bjDu0hIfH9cySGUzpTpl19yfqWUPiHnxANzPw3whxrGWHEv0ziRUx4shAuFhe1wEhXRPcnaDcUgG%2F5A051iRCTBseuRjylgij2ISmYyaftuMHIN8AueqvxHA18Heh0y%2FZS%2FQEUAO4slz9wNnla1LAgETU%2BnIvMAgUNfDWtiNsNbw%3D%3D--hcTV8oezlRezbQEs--Ob%2BBinxZgcKxiMHneb84jA%3D%3D; _gid=GA1.2.1106100520.1621335698; _gat_gtag_UA_122455023_2=1"})
    # session.headers.update({'Cookie': f'_lionwheel_session={_cookies[0]}; remember_user_token={_cookies[1]}'})


    ## Create delivery butik25

    create_delivery_csrf_token = set_csrf_and_cookies(
                        _type="tasks",
                         cookieFile=f'../config/tasks_{TYPE}_Cookies',
                         jsonFile=f'../config/tasks_{TYPE}_csrf.json',
                         url="https://members.lionwheel.com/tasks?locale=he")
    print(csrf_token)
    print()
    cookies_values = session.cookies.values()
    session.headers.update({'Cookie': f'_lionwheel_session={cookies_values[0]}; remember_user_token={cookies_values[1]}'})
    print(len(cookies_values), "values on list")
    # print(session.cookies)
    # print(session.headers)

    def create_delivery():
      url = "https://members.lionwheel.com/tasks?locale=he"

      # payload='authenticity_token=FYtw%2BU4FmFD0WN566na6lOMI8Cd%2BcTqFZSmrSCZ6Mqpy7sUJkMXnTFbYuuztVxaR3wiuKoXQPCQ%2FxrJQGuQYdg%3D%3D&button=&fixed_appear_time=6%3A00&task%5Bdestination_apartment%5D=&task%5Bdestination_city_other%5D=%D7%92%D7%93%D7%A8%D7%94&task%5Bdestination_email%5D=info%40spider3d.co.il&task%5Bdestination_floor%5D=&task%5Bdestination_location%5D=33787&task%5Bdestination_name%5D=%D7%A1%D7%A4%D7%99%D7%99%D7%93%D7%A8%20%D7%AA%D7%9C%D7%AA%20%D7%9E%D7%99%D7%9E%D7%93&task%5Bdestination_notes%5D=%D7%90%D7%99%D7%99%D7%9C%20-%20058-5551234&task%5Bdestination_number%5D=114&task%5Bdestination_phone%5D=0522509900&task%5Bdestination_recipient_name%5D=%D7%90%D7%A4%D7%A8%D7%AA%2F%D7%90%D7%99%D7%99%D7%9C&task%5Bdestination_street_other%5D=%D7%97%D7%91%D7%A7%D7%95%D7%A7&task%5Bdestination_zone%5D=&task%5Bdocument_number%5D=&task%5Bfixed_end_date%5D=31%2F12%2F2030&task%5Bfixed_start_date%5D=&task%5Bis_friday%5D=0&task%5Bis_monday%5D=0&task%5Bis_roundtrip%5D=0&task%5Bis_saturday%5D=0&task%5Bis_sunday%5D=0&task%5Bis_thursday%5D=0&task%5Bis_tuesday%5D=0&task%5Bis_wednesday%5D=0&task%5Bmoney_collect%5D=&task%5Bnotes%5D=&task%5Bpackages_quantity%5D=1&task%5Bsame_day%5D=0&task%5Bsave_destination_location%5D=0&task%5Bsave_source_location%5D=0&task%5Bsource_apartment%5D=&task%5Bsource_city%5D=&task%5Bsource_city_other%5D=&task%5Bsource_email%5D=&task%5Bsource_floor%5D=&task%5Bsource_location%5D=&task%5Bsource_name%5D=&task%5Bsource_notes%5D=&task%5Bsource_number%5D=&task%5Bsource_phone%5D=&task%5Bsource_recipient_name%5D=&task%5Bsource_street%5D=&task%5Bsource_street_other%5D=&task%5Bsource_zone%5D=&task%5Bsurfaces_quantity%5D=&task%5Btask_date%5D=18%2F05%2F2021&task%5Btiming_type%5D=timingNow&task%5Burgency%5D=REGULAR&task%5Bvehicle_kind%5D=SCOOTER'

      import json
      # payload = {
      #   'authenticity_token': create_delivery_csrf_token,
      #   'button': '',
      #   'fixed_appear_time': '6: 00',
      #   'task': {
      #     'destination_apartment': '',
      #     'destination_city_other': 'גדרה',
      #     'destination_email': 'info@spider3d.co.il',
      #     'destination_floor': '',
      #     'destination_location': '33787',
      #     'destination_name': 'ספיידרתלתמימד',
      #     'destination_notes': 'אייל-058-5551234',
      #     'destination_number': '114',
      #     'destination_phone': '0522509900',
      #     'destination_recipient_name': 'אפרת/אייל',
      #     'destination_street_other': 'חבקוק',
      #     'destination_zone': '',
      #     'document_number': '',
      #     'fixed_end_date': '31/12/2030',
      #     'fixed_start_date': '',
      #     'is_friday': '0',
      #     'is_monday': '0',
      #     'is_roundtrip': '0',
      #     'is_saturday': '0',
      #     'is_sunday': '0',
      #     'is_thursday': '0',
      #     'is_tuesday': '0',
      #     'is_wednesday': '0',
      #     'money_collect': '',
      #     'notes': '',
      #     'packages_quantity': '1',
      #     'same_day': '0',
      #     'save_destination_location': '0',
      #     'save_source_location': '0',
      #     'source_apartment': '',
      #     'source_city': '',
      #     'source_city_other': '',
      #     'source_email': '',
      #     'source_floor': '',
      #     'source_location': '',
      #     'source_name': '',
      #     'source_notes': '',
      #     'source_number': '',
      #     'source_phone': '',
      #     'source_recipient_name': '',
      #     'source_street': '',
      #     'source_street_other': '',
      #     'source_zone': '',
      #     'surfaces_quantity': '',
      #     'task_date': '18/05/2021',
      #     'timing_type': 'timingNow',
      #     'urgency': 'REGULAR',
      #     'vehicle_kind': 'SCOOTER'
      #   }
      # }
      # payload = json.dumps(payload)

      # payload = str(payload).replace("'", '"').encode()

      # from querystring_parser import builder as qsbuilder
      # payload = qsbuilder.build(payload).replace("[", "%5B").replace("]", "%5D")

      # destination_city_other : destination_street_other + packages_quantity
      payload=f'authenticity_token={create_delivery_csrf_token}' \
              f'&button=&' \
              f'fixed_appear_time=6%3A00&' \
              f'task%5B' \
              f'destination_apartment%5D=&' \
              f'task%5Bdestination_city_other%5D=%D7%92%D7%93%D7%A8%D7%94&' \
              f'task%5Bdestination_email%5D=info%40spider3d.co.il&' \
              f'task%5Bdestination_floor%5D=&' \
              f'task%5Bdestination_location%5D=33787&' \
              f'task%5Bdestination_name%5D=%D7%A1%D7%A4%D7%99%D7%99%D7%93%D7%A8%20%D7%AA%D7%9C%D7%AA%20%D7%9E%D7%99%D7%9E%D7%93&' \
              f'task%5Bdestination_notes%5D=%D7%90%D7%99%D7%99%D7%9C%20-%20058-5551234&' \
              f'task%5Bdestination_number%5D=114&' \
              f'task%5Bdestination_phone%5D=0522509900&' \
              f'task%5Bdestination_recipient_name%5D=%D7%90%D7%A4%D7%A8%D7%AA%2F%D7%90%D7%99%D7%99%D7%9C&' \
              f'task%5Bdestination_street_other%5D=%D7%97%D7%91%D7%A7%D7%95%D7%A7&' \
              f'task%5Bdestination_zone%5D=&' \
              f'task%5Bdocument_number%5D=&' \
              f'task%5Bfixed_end_date%5D=31%2F12%2F2030&' \
              f'task%5Bfixed_start_date%5D=&' \
              f'task%5Bis_friday%5D=0&' \
              f'task%5Bis_monday%5D=0&' \
              f'task%5Bis_roundtrip%5D=0&' \
              f'task%5Bis_saturday%5D=0&' \
              f'task%5Bis_sunday%5D=0&' \
              f'task%5Bis_thursday%5D=0&' \
              f'task%5Bis_tuesday%5D=0&' \
              f'task%5Bis_wednesday%5D=0&' \
              f'task%5Bmoney_collect%5D=&' \
              f'task%5Bnotes%5D=&' \
              f'task%5Bpackages_quantity%5D=1&' \
              f'task%5Bsame_day%5D=0&' \
              f'task%5Bsave_destination_location%5D=0&' \
              f'task%5Bsave_source_location%5D=0&' \
              f'task%5Bsource_apartment%5D=&' \
              f'task%5Bsource_city%5D=&' \
              f'task%5Bsource_city_other%5D=&' \
              f'task%5Bsource_email%5D=&' \
              f'task%5Bsource_floor%5D=&' \
              f'task%5Bsource_location%5D=&' \
              f'task%5Bsource_name%5D=&' \
              f'task%5Bsource_notes%5D=&' \
              f'task%5Bsource_number%5D=&' \
              f'task%5Bsource_phone%5D=&' \
              f'task%5Bsource_recipient_name%5D=&' \
              f'task%5Bsource_street%5D=&' \
              f'task%5Bsource_street_other%5D=&' \
              f'task%5Bsource_zone%5D=&' \
              f'task%5Bsurfaces_quantity%5D=&' \
              f'task%5Btask_date%5D=18%2F05%2F2021&t' \
              f'ask%5Btiming_type%5D=timingNow&' \
              f'task%5Burgency%5D=REGULAR&' \
              f'task%5Bvehicle_kind%5D=SCOOTER'

      # headers = {
      #  'Cookie': f'_lionwheel_session={cookies_values[0]}; remember_user_token={cookies_values[1]}'
      # }

      # session.headers.update({'Cookie': f'_lionwheel_session={cookies_values[0]}; remember_user_token={cookies_values[1]}'})

      response = session.post(url,
                              # headers=headers, # No Need, already in session
                              data=payload)

      # print("response.text Has been copied to clipboard")
      # pyperclip.copy(response.text)
      if response.status_code == 200:
        print(response.status_code)
        print("Delivery has been created successfully")
      else:
          print(response.status_code)
          print(response.text[30:90]) #  <title>The change you wanted was rejected (422)</title>
      return  response.status_code
      # print(response.request.headers)
    _status_code = create_delivery()

    return _status_code

status_code = main_delivery()
if status_code == 422:
    print("-------------------------------------------")
    shutil.rmtree("../config")  # removes not empty directory and its content
    # os.mkdir('../config') # create empty dir
    main_delivery()









