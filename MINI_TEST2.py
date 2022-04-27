from pprint import pprint

pen_history = {'data': []}
pen_history = []


pen_history.append( {
        'msg_id': 55,
        'msg_content': 'lol is cool',
        'user_id': 234565,
        'user_nickname': 'The Biton',
        'time_str': 234565,
    })
for item in pen_history:
        if 'x' != item['msg_content']:
                print('XXX')

pprint(pen_history)
