from pprint import pprint

from sqlalchemy import true, false, null

resp_form = {
  'post_type': [
    'product',
    'category',
    'category'
  ],
  'slider_num': [
    '1',
    '1',
    '2'
  ],
  'post_num': [
    '12345',
    '12345',
    '23451'
  ],
  'pic_link': [
    'www11',
    'www11',
    'www2'
  ]
}

# print(resp.keys())

items_dict = {}
forIndex = 0
## 1 Setup inner dict to place "items" list
# EXAMPLE: {'1': {'items': []}, '2': {'items': []}}
for item in resp_form["slider_num"]: # post_type represent the quantity of rows on control panel
  items_dict.update({
  resp_form["slider_num"][forIndex]: {"items": []},
  })
  forIndex += 1



## 2 place "items" on the right slider
# EXAMPLE: {'1': {'items': [{'category': '12111', 'image': 'www12', 'padding': 15.0, 'my_slider_num': '1'}]}, '2': {'items': [{'category': '23451', 'image': 'www2', 'padding': 15.0, 'my_slider_num': '2'}]}}
forIndex = 0
for item in resp_form["slider_num"]: # post_type represent the quantity of rows on control panel
  items_dict[ resp_form["slider_num"][forIndex]] \
  ["items"].append({
    resp_form["post_type"][forIndex]: resp_form["post_num"][forIndex],
    "image": resp_form["pic_link"][forIndex],
    "padding": 15.0,
    # "my_slider_num": resp["slider_num"][forIndex],
  })
  forIndex += 1


# print(items_dict)

import urllib.request, json
with urllib.request.urlopen("https://config-fluxstore-47g7m0odz-idan054.vercel.app/") as url:
  try:
    full_config = json.loads(url.read().decode())
  except:
    full_config = url.read()

## place final "items" of full config
forIndex = 0
for item in full_config["HorizonLayout"]:
  # print(item)
  if item["layout"] == "bannerImage":
    try:
      # print(full_config["HorizonLayout"][forIndex]["items"])
      print(forIndex)
      full_config["HorizonLayout"][forIndex]["items"] = \
      items_dict[f"{forIndex}"]["items"]
    except: pass
  forIndex += 1
# print(full_config["HorizonLayout"])
full_config = json.dumps(full_config, indent=1, ensure_ascii=False)
print(full_config)

sample =      """{
      "layout": "bannerImage",
      "isSlider": true,
      "autoPlay": true,
      "showNumber": false,
      "design": "default",
      "showBackGround": true,
      "radius": 8,
      "items": [
        {
          "product": 25056,
          "image": "https://i.imgur.com/84ySdG3.jpg",
          "padding": 15.0
        }
      ]
    },
    {
      "layout": "bannerImage",
      "isSlider": true,
      "autoPlay": true,
      "showNumber": false,
      "design": "default",
      "showBackGround": true,
      "radius": 8,
      "items": [
        {
          "category": 4783,
          "image": "https://i.imgur.com/H0bcI9u.jpg",
          "padding": 15.0
        },
        {
          "category": 2352,
          "image": "https://i.imgur.com/H7BJGsh.jpg",
          "padding": 15.0
        }
      ]
    },"""