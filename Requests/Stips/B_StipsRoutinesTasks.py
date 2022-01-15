from time import sleep
import requests
import json
from color_printer import *


# a funcs that need to be in While True
class StipsRoutinesTasks:
    # Set changeable Values: loginData = LoginStips(session, 'idan@', 'mypass')
    def __init__(self, session, user, password):
        # def __init__(self, session= None, user= 'x', password ='x'):
        # def __init__(self, user=10, password='idan default'):
        self.session = session
        self.userEmail = user
        self.password = password

    # Check if current user have new notifications
    def get_notifications(self, isPrinting):
        session = self.session
        user = self.userEmail
        password = self.password

        # print("get_api_data()")
        # Remember: the cookie already embed in the sesssion

        # Cookie has been set by the session
        res = session.get("https://stips.co.il/api?name=messages.count&api_params=%7B%7D")
        res_dict = json.loads(res.text)
        notificationsCount = res_dict["data"]["notificationsCount"]
        messagesCount = res_dict["data"]["messagesCount"]
        if isPrinting \
                and messagesCount != 0:
            # or notificationsCount != 0:
            printGreen(
                f'User {self.userEmail} Have 📱 {messagesCount} massages & 🔔 {notificationsCount} notifications.')
        elif isPrinting:  # (and messagesCount = 0)
            printGrey(f'User {self.userEmail} Have 0 new massages 📱.')

        # printBlue(res.text)
        # printGreen(f"🔔 notificationsCount is {notificationsCount}")
        # printGreen(f"📱 messagesCount is {messagesCount}")
        return notificationsCount, messagesCount

    # Check if specific user is online
    def check_online_user(self, userId):
        session = self.session
        user = self.userEmail
        password = self.password

        from pprint import pprint
        # response = session.get('https://stips.co.il/api?name=omniobj&rest_action=GET&omniobj={"objType":"user","data":{"id":146235}}')
        res = session.get(
            # 'https://stips.co.il/api?name=omniobj&rest_action=GET&omniobj={"objType":"user","data":{"id":290006}}')
            'https://stips.co.il/api?name=omniobj&rest_action=GET&omniobj={"objType":"user","data":{"id":' +
            f'{userId}' + '}}')
        # pprint(response.status_code)
        res_dict = json.loads(res.text)
        # print(res_dict)
        user_nick = res_dict['data']['omniOmniObj']['extra']['item_profile']['nickname']
        user_online_status = res_dict['data']['omniOmniObj']['extra']['item_profile']['online']

        # print('User 337166, AKA  "The Biton" is currently Online ✅')
        # print('User 337166, AKA  "The Biton" is currently Offline 🌚')
        # print(f'User {user_nick} online status is ')
        if user_online_status:
            printGreen(f'User "{user_nick}" is currently Online ✅')
        else:
            printGrey(f'User "{user_nick}" is currently Offline 🌚')

    # check_online_user()
    def get_pen_msgs(self, current_user_id, pen_history = []):
        session = self.session
        user = self.userEmail
        password = self.password

        # response = session.get('https://stips.co.il/api?name=objectlist&api_params=%7B%22method%22:%22penfriendsitem.new%22,%22page%22:1%7D')
        res = session.get('https://stips.co.il/api?name=objectlist&api_params={"method":"penfriendsitem.new","page":1}')
        # pprint(response.status_code)
        pen_msgs = json.loads(res.text)
        # print(pen_msgs)

        forIndex = 0
        for item in pen_msgs['data']:
            i = forIndex
            # Change pen_msgs["data"][i]["data"] -> item[i]
            msg_id = pen_msgs["data"][i]["data"]["id"]
            msg_content = pen_msgs["data"][i]["data"]["msg"]
            user_id = pen_msgs["data"][i]["data"]["userid"]
            user_nickname = pen_msgs["data"][i]["extra"]["item_profile"]["nickname"]
            time_str = pen_msgs["data"][i]["data"]["userid"]

            # print(f'user_id {user_id} OOO current_user_id {current_user_id}')
            # print(type(user_id), type(current_user_id))
            if f'{user_id}' == current_user_id:  # if pen-msg is from current user
                # print(f'user_id {user_id} = current_user_id {current_user_id}')
                in_pen_history = False
                for history_item in pen_history:
                    # print(f'msg_id {msg_id} {type(msg_id)} = history_item["msg_id"] {history_item["msg_id"]} {type(history_item["msg_id"])}')
                    if msg_id == history_item['msg_id']: in_pen_history = True
                if not in_pen_history:
                    pen_history.append({
                        'msg_id': msg_id,
                        'msg_content': msg_content,
                        'user_id': user_id,
                        'user_nickname': user_nickname,
                        'time_str': time_str,
                    })
                    # printGreen(f'{user_nickname}: {msg_content}\npen-msg Added.')

            forIndex += 1

        printGreen(f'Ur pen messages history: ({len(pen_history)})')
        for _item in pen_history:
            printGreen(_item["msg_content"])
            # printGreen(_item["msg_id"])

        return pen_history
