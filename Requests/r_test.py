create_delivery_csrf_token = "CNizcS2G+VtYf8s+wmNUapNjO/tWKOaqi6hcCs8iDmSq2likgtkMdLsn/+3IHX7toisZgxwnaVnagz+9DcTg0A=="

x = f"authenticity_token={create_delivery_csrf_token}&button=&fixed_appear_time=6%3A00&task%5Bdestination_apartment%5D=&task%5Bdestination_city_other%5D=%D7%92%D7%93%D7%A8%D7%94&task%5Bdestination_email%5D=info%40spider3d.co.il&task%5Bdestination_floor%5D=&task%5Bdestination_location%5D=33787&task%5Bdestination_name%5D=%D7%A1%D7%A4%D7%99%D7%99%D7%93%D7%A8%20%D7%AA%D7%9C%D7%AA%20%D7%9E%D7%99%D7%9E%D7%93&task%5Bdestination_notes%5D=%D7%90%D7%99%D7%99%D7%9C%20-%20058-5551234&task%5Bdestination_number%5D=114&task%5Bdestination_phone%5D=0522509900&task%5Bdestination_recipient_name%5D=%D7%90%D7%A4%D7%A8%D7%AA%2F%D7%90%D7%99%D7%99%D7%9C&task%5Bdestination_street_other%5D=%D7%97%D7%91%D7%A7%D7%95%D7%A7&task%5Bdestination_zone%5D=&task%5Bdocument_number%5D=&task%5Bfixed_end_date%5D=31%2F12%2F2030&task%5Bfixed_start_date%5D=&task%5Bis_friday%5D=0&task%5Bis_monday%5D=0&task%5Bis_roundtrip%5D=0&task%5Bis_saturday%5D=0&task%5Bis_sunday%5D=0&task%5Bis_thursday%5D=0&task%5Bis_tuesday%5D=0&task%5Bis_wednesday%5D=0&task%5Bmoney_collect%5D=&task%5Bnotes%5D=&task%5Bpackages_quantity%5D=1&task%5Bsame_day%5D=0&task%5Bsave_destination_location%5D=0&task%5Bsave_source_location%5D=0&task%5Bsource_apartment%5D=&task%5Bsource_city%5D=&task%5Bsource_city_other%5D=&task%5Bsource_email%5D=&task%5Bsource_floor%5D=&task%5Bsource_location%5D=&task%5Bsource_name%5D=&task%5Bsource_notes%5D=&task%5Bsource_number%5D=&task%5Bsource_phone%5D=&task%5Bsource_recipient_name%5D=&task%5Bsource_street%5D=&task%5Bsource_street_other%5D=&task%5Bsource_zone%5D=&task%5Bsurfaces_quantity%5D=&task%5Btask_date%5D=18%2F05%2F2021&task%5Btiming_type%5D=timingNow&task%5Burgency%5D=REGULAR&task%5Bvehicle_kind%5D=SCOOTER"
#

import json

payload = {
    'authenticity_token': create_delivery_csrf_token,
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

print(payload)
payload = json.dumps(payload)
print("------")
print(payload)

# from querystring_parser import builder as qsbuilder
# payload = qsbuilder.build(payload).replace("%22%3A%20%22", "=") #.replace("[", "%5B").replace("]", "%5D")
#
# print(len(x))
# print(x)
# print(len(payload))
# print(payload)

# authenticity_token=CNizcS2G+VtYf8s+wmNUapNjO/tWKOaqi6hcCs8iDmSq2likgtkMdLsn/+3IHX7toisZgxwnaVnagz+9DcTg0A==&button=&fixed_appear_time=6%3A00&task%5Bdestination_apartment%5D=&task%5Bdestination_city_other%5D=%D7%92%D7%93%D7%A8%D7%94&task%5Bdestination_email%5D=info%40spider3d.co.il&task%5Bdestination_floor%5D=&task%5Bdestination_location%5D=33787&task%5Bdestination_name%5D=%D7%A1%D7%A4%D7%99%D7%99%D7%93%D7%A8%20%D7%AA%D7%9C%D7%AA%20%D7%9E%D7%99%D7%9E%D7%93&task%5Bdestination_notes%5D=%D7%90%D7%99%D7%99%D7%9C%20-%20058-5551234&task%5Bdestination_number%5D=114&task%5Bdestination_phone%5D=0522509900&task%5Bdestination_recipient_name%5D=%D7%90%D7%A4%D7%A8%D7%AA%2F%D7%90%D7%99%D7%99%D7%9C&task%5Bdestination_street_other%5D=%D7%97%D7%91%D7%A7%D7%95%D7%A7&task%5Bdestination_zone%5D=&task%5Bdocument_number%5D=&task%5Bfixed_end_date%5D=31%2F12%2F2030&task%5Bfixed_start_date%5D=&task%5Bis_friday%5D=0&task%5Bis_monday%5D=0&task%5Bis_roundtrip%5D=0&task%5Bis_saturday%5D=0&task%5Bis_sunday%5D=0&task%5Bis_thursday%5D=0&task%5Bis_tuesday%5D=0&task%5Bis_wednesday%5D=0&task%5Bmoney_collect%5D=&task%5Bnotes%5D=&task%5Bpackages_quantity%5D=1&task%5Bsame_day%5D=0&task%5Bsave_destination_location%5D=0&task%5Bsave_source_location%5D=0&task%5Bsource_apartment%5D=&task%5Bsource_city%5D=&task%5Bsource_city_other%5D=&task%5Bsource_email%5D=&task%5Bsource_floor%5D=&task%5Bsource_location%5D=&task%5Bsource_name%5D=&task%5Bsource_notes%5D=&task%5Bsource_number%5D=&task%5Bsource_phone%5D=&task%5Bsource_recipient_name%5D=&task%5Bsource_street%5D=&task%5Bsource_street_other%5D=&task%5Bsource_zone%5D=&task%5Bsurfaces_quantity%5D=&task%5Btask_date%5D=18%2F05%2F2021&task%5Btiming_type%5D=timingNow&task%5Burgency%5D=REGULAR&task%5Bvehicle_kind%5D=SCOOTER
# %7B%22authenticity_token=CNizcS2G%2BVtYf8s%2BwmNUapNjO/tWKOaqi6hcCs8iDmSq2likgtkMdLsn/%2B3IHX7toisZgxwnaVnagz%2B9DcTg0A%3D%3D%22%2C%20%22button=%22%2C%20%22fixed_appear_time=6%3A%2000%22%2C%20%22task%22%3A%20%7B%22destination_apartment=%22%2C%20%22destination_city_other=%5Cu05d2%5Cu05d3%5Cu05e8%5Cu05d4%22%2C%20%22destination_email=info%40spider3d.co.il%22%2C%20%22destination_floor=%22%2C%20%22destination_location=33787%22%2C%20%22destination_name=%5Cu05e1%5Cu05e4%5Cu05d9%5Cu05d9%5Cu05d3%5Cu05e8%5Cu05ea%5Cu05dc%5Cu05ea%5Cu05de%5Cu05d9%5Cu05de%5Cu05d3%22%2C%20%22destination_notes=%5Cu05d0%5Cu05d9%5Cu05d9%5Cu05dc-058-5551234%22%2C%20%22destination_number=114%22%2C%20%22destination_phone=0522509900%22%2C%20%22destination_recipient_name=%5Cu05d0%5Cu05e4%5Cu05e8%5Cu05ea/%5Cu05d0%5Cu05d9%5Cu05d9%5Cu05dc%22%2C%20%22destination_street_other=%5Cu05d7%5Cu05d1%5Cu05e7%5Cu05d5%5Cu05e7%22%2C%20%22destination_zone=%22%2C%20%22document_number=%22%2C%20%22fixed_end_date=31/12/2030%22%2C%20%22fixed_start_date=%22%2C%20%22is_friday=0%22%2C%20%22is_monday=0%22%2C%20%22is_roundtrip=0%22%2C%20%22is_saturday=0%22%2C%20%22is_sunday=0%22%2C%20%22is_thursday=0%22%2C%20%22is_tuesday=0%22%2C%20%22is_wednesday=0%22%2C%20%22money_collect=%22%2C%20%22notes=%22%2C%20%22packages_quantity=1%22%2C%20%22same_day=0%22%2C%20%22save_destination_location=0%22%2C%20%22save_source_location=0%22%2C%20%22source_apartment=%22%2C%20%22source_city=%22%2C%20%22source_city_other=%22%2C%20%22source_email=%22%2C%20%22source_floor=%22%2C%20%22source_location=%22%2C%20%22source_name=%22%2C%20%22source_notes=%22%2C%20%22source_number=%22%2C%20%22source_phone=%22%2C%20%22source_recipient_name=%22%2C%20%22source_street=%22%2C%20%22source_street_other=%22%2C%20%22source_zone=%22%2C%20%22surfaces_quantity=%22%2C%20%22task_date=18/05/2021%22%2C%20%22timing_type=timingNow%22%2C%20%22urgency=REGULAR%22%2C%20%22vehicle_kind=SCOOTER%22%7D%7D