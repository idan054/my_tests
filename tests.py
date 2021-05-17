message_details = {
  'message_id': 80,
  'from': {
    'id': 429798438,
    'is_bot': False,
    'first_name': 'TheBlackHero™',
    'username': 'TheBlackHero55',
    'language_code': 'en'
  },
  'chat': {
    'id': 429798438,
    'first_name': 'TheBlackHero™',
    'username': 'TheBlackHero55',
    'type': 'private'
  },
  'date': 1621257947,
  'text': '/is_online',
  'entities': [
    {
      'offset': 0,
      'length': 10,
      'type': 'bot_command'
    }
  ]
}

if message_details["text"] == "/is_online":
    print(message_details["chat"]["username"])
    print(message_details["chat"]["id"])