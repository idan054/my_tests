from bs4 import BeautifulSoup, SoupStrainer
import datetime
import requests
import gspread


session = requests.session()
start_time = datetime.datetime.now()
print(start_time.strftime("%d/%m/%Y %H:%M:%S"))
resp = session.get('https://easy.co.il/json/list.json?listpage=2&c=17440&c2=15140&c3=4968')
if resp.status_code != 200:
    biz_list = []
    print("STATUS CODE ERR ", resp.status_code)
else:
    print(resp.status_code)
    biz_list = resp.json()['bizlist']['list']
    # print(biz_list)

easy_biz_links = []
for i in biz_list:
    easy_biz_links.append(f'https://easy.co.il{i["url"]}')
print(easy_biz_links)

# print('1')
# print(biz_list['logo'])
# print(biz_list['bizname'])
# print(biz_list['actions'][0]['link'])
# print(biz_list['address'])
# print('מייל')
# print('הערות')
# print(biz_list['phone'])
# print('IG')
# print('FB')
# print(str(biz_list['url']).replace('/page/', ''))
# print(f"https://easy.co.il{biz_list['url']}")
# print('ביקורים החודש')
# print('similarweb')


# for i in shop_list:

gc = gspread.service_account()

# Open a sheet from a spreadsheet in one go
# wks = gc.open("Where is the money Lebowski?").sheet1
sht1 = gc.open_by_key('1qX31t2nKxVpDgbaSN5c1q4YUYLR2KqedV2CZrtvohKA').get_worksheet(0)

# Update a range of cells using the top left corner address
# sht1.update('A1', [[1, 2], [3, 4]])
# Format the header
# sht1.format('A1:B1', {'textFormat': {'bold': True}})


for biz in biz_list:
    current_row = len(sht1.col_values(3)) + 1  # AKA Column 'C'
    print(f'current_row: {current_row}')
    action_link = str(biz['actions'][0]['link'])
    fb_link = ''
    if 'facebook' in action_link:
        fb_link = action_link
        action_link = ''


    # Or update a single cell
    sht1.update(f'A{current_row}:N{current_row}', [[
    f'{current_row}',                            # מס' שורה
    f'=IMAGE(\"{str(biz["logo"])}\", 2)',       # לוגו העסק
    biz['bizname'],                             # שם העסק
    action_link,                                # קישור לעסק
    biz['address'],                             # כתובת
    '',                                         # מייל
    '',                                         # הערות
    biz['phone'],                               # טלפון
    '',                                         # אינסטגם
    fb_link,                                    # פייסבוק
    str(biz['url']).replace('/page/', ''),      # מס עסק איזי
    f"https://easy.co.il{biz['url']}",          # קישור איזי
    '',                                         # ביקורים החודש בחנות פיזית
    '',                                         # similarweb - ביקורים החודש
    ]])

print('Done.')

    # מס'
    # לוגו
    # שם העסק
    # קישור
    # ממוקם בעיר
    # מייל
    # הערות
    # טלפון דרך איזי
    # אינסטגרם
    # פייסבוק
    # מס' עסק איזי
    # קישור איזי
    # ביקורים החודש
    # similarweb