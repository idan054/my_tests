from bs4 import BeautifulSoup, SoupStrainer
from pprint import pprint
import requests, pickle
import json
import os
import shutil
import random

original_order_id = f"Spider3D {str(random.randint(1, 1000))}"
print(original_order_id)

def create_delivery():
    session = requests.session()
    # url = "https://members.lionwheel.com/tasks?locale=he?key=c_key_3694a9a7-6993-4d4a-8016-cedf0759f9eb"
    url = " https://members.lionwheel.com/api/v1/tasks/create?key=c_key_3694a9a7-6993-4d4a-8016-cedf0759f9eb"

    payload = {
        "pickup_at": "16/07/2021",
        'original_order_id': original_order_id,
        'notes': '',
        'packages_quantity': '2',

        # 'source_city': 'גדרה',
        # 'source_street': 'חבקוק',
        # 'source_number': '114',
        # 'source_floor': '',
        # 'source_apartment': '',
        # 'source_notes': 'אייל-058-5551234',
        # 'source_recipient_name': 'אפרת/אייל',
        # 'source_phone': '0522509900',
        # 'source_email': 'info@spider3d.co.il',
        # 'source_city_other': 'גדרה',
        # 'source_city_other': '',
        # 'source_location': '',
        # 'source_name': '',
        # 'source_street_other': '',
        # 'source_zone': '',

        'destination_city': 'גדרה',
        'destination_street': 'חבקוק',
        'destination_number': '114',
        'destination_floor': '',
        'destination_apartment': '',
        'destination_notes': 'אייל-058-5551234',
        'destination_recipient_name': 'אפרת/אייל',
        'destination_phone': '0522509900',
        'destination_email': 'info@spider3d.co.il',
        # 'destination_city_other': 'גדרה',
        # 'destination_location': '33787',
        # 'destination_name': 'ספיידרתלתמימד',
        # 'destination_zone': '',
        # 'destination_street_other': 'חבקוק',

        ## Others by the API Docs ##
        # ==========================
        # 'company_id': '',
        # 'delivery_method'
        # 'greeting'
        # 'gifter_name'
        # 'gifter_phone'
        # 'is_roundtrip'

        ## Others by the Butik 24 POST ##
        # ===============================
        #     'surfaces_quantity': '',
        #     'task_date': '18/05/2021',
        #     'timing_type': 'timingNow',
        #     'urgency': 'REGULAR',
        #     'vehicle_kind': 'SCOOTER'
        #     'document_number': '',
        #     'fixed_end_date': '31/12/2030',
        #     'fixed_start_date': '',
        #     'money_collect': '',
        #     'notes': '',
        #     'packages_quantity': '1',
        #     'same_day': '0',
        #     'save_destination_location': '0',
        #     'save_source_location': '0',
    }

    # payload='authenticity_token=FYtw%2BU4FmFD0WN566na6lOMI8Cd%2BcTqFZSmrSCZ6Mqpy7sUJkMXnTFbYuuztVxaR3wiuKoXQPCQ%2FxrJQGuQYdg%3D%3D&button=&fixed_appear_time=6%3A00&task%5Bdestination_apartment%5D=&task%5Bdestination_city_other%5D=%D7%92%D7%93%D7%A8%D7%94&task%5Bdestination_email%5D=info%40spider3d.co.il&task%5Bdestination_floor%5D=&task%5Bdestination_location%5D=33787&task%5Bdestination_name%5D=%D7%A1%D7%A4%D7%99%D7%99%D7%93%D7%A8%20%D7%AA%D7%9C%D7%AA%20%D7%9E%D7%99%D7%9E%D7%93&task%5Bdestination_notes%5D=%D7%90%D7%99%D7%99%D7%9C%20-%20058-5551234&task%5Bdestination_number%5D=114&task%5Bdestination_phone%5D=0522509900&task%5Bdestination_recipient_name%5D=%D7%90%D7%A4%D7%A8%D7%AA%2F%D7%90%D7%99%D7%99%D7%9C&task%5Bdestination_street_other%5D=%D7%97%D7%91%D7%A7%D7%95%D7%A7&task%5Bdestination_zone%5D=&task%5Bdocument_number%5D=&task%5Bfixed_end_date%5D=31%2F12%2F2030&task%5Bfixed_start_date%5D=&task%5Bis_friday%5D=0&task%5Bis_monday%5D=0&task%5Bis_roundtrip%5D=0&task%5Bis_saturday%5D=0&task%5Bis_sunday%5D=0&task%5Bis_thursday%5D=0&task%5Bis_tuesday%5D=0&task%5Bis_wednesday%5D=0&task%5Bmoney_collect%5D=&task%5Bnotes%5D=&task%5Bpackages_quantity%5D=1&task%5Bsame_day%5D=0&task%5Bsave_destination_location%5D=0&task%5Bsave_source_location%5D=0&task%5Bsource_apartment%5D=&task%5Bsource_city%5D=&task%5Bsource_city_other%5D=&task%5Bsource_email%5D=&task%5Bsource_floor%5D=&task%5Bsource_location%5D=&task%5Bsource_name%5D=&task%5Bsource_notes%5D=&task%5Bsource_number%5D=&task%5Bsource_phone%5D=&task%5Bsource_recipient_name%5D=&task%5Bsource_street%5D=&task%5Bsource_street_other%5D=&task%5Bsource_zone%5D=&task%5Bsurfaces_quantity%5D=&task%5Btask_date%5D=18%2F05%2F2021&task%5Btiming_type%5D=timingNow&task%5Burgency%5D=REGULAR&task%5Bvehicle_kind%5D=SCOOTER'
    # payload = f'authenticity_token={tasks_csrfToken}&button=&fixed_appear_time=6%3A00&task%5Bdestination_apartment%5D=&task%5Bdestination_city_other%5D=%D7%92%D7%93%D7%A8%D7%94&task%5Bdestination_email%5D=info%40spider3d.co.il&task%5Bdestination_floor%5D=&task%5Bdestination_location%5D=33787&task%5Bdestination_name%5D=%D7%A1%D7%A4%D7%99%D7%99%D7%93%D7%A8%20%D7%AA%D7%9C%D7%AA%20%D7%9E%D7%99%D7%9E%D7%93&task%5Bdestination_notes%5D=%D7%90%D7%99%D7%99%D7%9C%20-%20058-5551234&task%5Bdestination_number%5D=114&task%5Bdestination_phone%5D=0522509900&task%5Bdestination_recipient_name%5D=%D7%90%D7%A4%D7%A8%D7%AA%2F%D7%90%D7%99%D7%99%D7%9C&task%5Bdestination_street_other%5D=%D7%97%D7%91%D7%A7%D7%95%D7%A7&task%5Bdestination_zone%5D=&task%5Bdocument_number%5D=&task%5Bfixed_end_date%5D=31%2F12%2F2030&task%5Bfixed_start_date%5D=&task%5Bis_friday%5D=0&task%5Bis_monday%5D=0&task%5Bis_roundtrip%5D=0&task%5Bis_saturday%5D=0&task%5Bis_sunday%5D=0&task%5Bis_thursday%5D=0&task%5Bis_tuesday%5D=0&task%5Bis_wednesday%5D=0&task%5Bmoney_collect%5D=&task%5Bnotes%5D=&task%5Bpackages_quantity%5D=1&task%5Bsame_day%5D=0&task%5Bsave_destination_location%5D=0&task%5Bsave_source_location%5D=0&task%5Bsource_apartment%5D=&task%5Bsource_city%5D=&task%5Bsource_city_other%5D=&task%5Bsource_email%5D=&task%5Bsource_floor%5D=&task%5Bsource_location%5D=&task%5Bsource_name%5D=&task%5Bsource_notes%5D=&task%5Bsource_number%5D=&task%5Bsource_phone%5D=&task%5Bsource_recipient_name%5D=&task%5Bsource_street%5D=&task%5Bsource_street_other%5D=&task%5Bsource_zone%5D=&task%5Bsurfaces_quantity%5D=&task%5Btask_date%5D=18%2F05%2F2021&task%5Btiming_type%5D=timingNow&task%5Burgency%5D=REGULAR&task%5Bvehicle_kind%5D=SCOOTER'

    import json
    # payload = json.dumps(payload)

    # from querystring_parser import builder as qsbuilder
    # payload = qsbuilder.build(payload)  # .replace("[", "%5B").replace("]", "%5D")
    # print(payload)

    response = session.post(url,
                            # headers=headers,  # No Need, already in session
                            data=payload)

    # print("response.text Has been copied to clipboard")
    # pyperclip.copy(response.text)
    if response.status_code == 200:
        print(response.status_code)
        # print(response.text)
        print("Delivery has been created successfully")
    else:
        print(response.status_code)
        print(response.text)  # <title>The change you wanted was rejected (422)</title>
    return response.status_code
    # print(response.request.headers)

_status_code = create_delivery()
print(_status_code)






