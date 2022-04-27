
import datetime
import datetime
# Create a new client
import json
from pprint import pprint

import stream
# client = stream.connect('YOUR_API_KEY', 'API_KEY_SECRET')
client = stream.connect('ah48ckptkjvm',
						'gfcfa94ghkctn3du36s2d4nmqg9q24wtxhr56qd84pj7dum94ahhtedccj8q7wk4')

# For the feed group 'user' and user id 'eric' get the feed
eric_feed = client.feed('test_uesr', 'eric')

# Get activities from 5 to 10 (slow pagination)
# result = eric_feed.get(limit=5, offset=5)

# static result to save requests
# result = {'results': [{'actor': '1', 'course': {'distance': 10, 'name': 'Golden Gate park'}, 'foreign_id': 'run:1', 'id': 'e2a32d34-85cc-11ec-807a-025b47ecba9d', 'object': '1', 'origin': None, 'participants': ['Thierry', 'Tommaso'], 'started_at': datetime.datetime(2022, 2, 4, 15, 12, 35, 412824, tzinfo=<UTC>), 'target': '', 'time': datetime.datetime(2022, 2, 4, 15, 12, 36, 381010, tzinfo=<UTC>), 'verb': 'run'}, {'actor': 'eric', 'foreign_id': '', 'id': '70d3700c-85cb-11ec-a64e-0668c1aa6cf1', 'object': '1', 'origin': None, 'target': '', 'time': datetime.datetime(2022, 2, 4, 15, 2, 15, 940302, tzinfo=<UTC>), 'tweet': 'Hello world', 'verb': 'tweet'}, {'actor': 'eric', 'foreign_id': '', 'id': 'b465bfd6-858b-11ec-b8b0-0aedede70789', 'object': '1', 'origin': None, 'target': '', 'time': datetime.datetime(2022, 2, 4, 7, 26, 1, 515823, tzinfo=<UTC>), 'tweet': 'Hello world', 'verb': 'tweet'}, {'actor': 'eric', 'foreign_id': '', 'id': '7cd8bb42-858b-11ec-b89c-0aedede70789', 'object': '1', 'origin': None, 'target': '', 'time': datetime.datetime(2022, 2, 4, 7, 24, 28, 316960, tzinfo=<UTC>), 'tweet': 'Hello world', 'verb': 'tweet'}, {'actor': 'eric', 'foreign_id': '', 'id': '415f7afa-858b-11ec-afe6-0668c1aa6cf1', 'object': '1', 'origin': None, 'target': '', 'time': datetime.datetime(2022, 2, 4, 7, 22, 48, 536755, tzinfo=<UTC>), 'tweet': 'Hello world', 'verb': 'tweet'}], 'next': '', 'duration': '8.26ms'}
# (Recommended & faster) Filter on an id less than the given UUID
# result = eric_feed.get(limit=5, id_lt="e561de8f-00f1-11e4-b400-0cc47a024be0")


# Add the activity to the feed
activity_data = {'actor': 1, 'verb': 'run', 'object': 1, 'foreign_id': 'run:1',
	'course': {'name': 'Golden Gate park', 'distance': 10},
	'participants': ['Thierry', 'Tommaso'],
	'started_at': datetime.datetime.now()
}
# activity_response = eric_feed.add_activity(activity_data)
# activity_response = eric_feed.add_activity(activity_data)
# eric_feed.remove_activity(activity_data)
# eric_feed.remove_activity(activity_id='70d3700c-85cb-11ec-a64e-0668c1aa6cf1')
result = eric_feed.get()
print('result')
print(len(result)) # dict
pprint(result) # dict
# print(json.loads(result))

# with open('result.json', 'w') as fp:
#     json.dump(result, fp)

# print('activity_response')
# print(activity_response)


