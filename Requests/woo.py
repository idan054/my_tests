from woocommerce import API

spiderUrl = 'https://spider3d.co.il'

wcapi = API(
    url=spiderUrl,
    consumer_key="consumer_key",
    consumer_secret="consumer_secret",
    wp_api=True,
    version="wc/v2"
)

resp = wcapi.get('/wp-json/wc/v2/orders').json()
print(resp)

#     "url": "https://spider3d.co.il",
#     "consumerSecret": "cs_828fd108ff909e5aff0be3be11d3df07503a3a87",
#     "type": "woo",
#     "consumerKey": "ck_41073388529656e637ba4c497237a3f0f34bd2a9"