from pprint import pprint

from sqlalchemy import true, false, null

resp = {
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
for item in resp["slider_num"]: # post_type represent the quantity of rows on control panel
  items_dict.update({
  resp["slider_num"][forIndex]: {"items": []},
  })
  forIndex += 1



## 2 place "items" on the right slider
# EXAMPLE: {'1': {'items': [{'category': '12111', 'image': 'www12', 'padding': 15.0, 'my_slider_num': '1'}]}, '2': {'items': [{'category': '23451', 'image': 'www2', 'padding': 15.0, 'my_slider_num': '2'}]}}
forIndex = 0
for item in resp["slider_num"]: # post_type represent the quantity of rows on control panel
  items_dict[ resp["slider_num"][forIndex] ] \
  ["items"].append({
    resp["post_type"][forIndex]: resp["post_num"][forIndex],
    "image": resp["pic_link"][forIndex],
    "padding": 15.0,
    # "my_slider_num": resp["slider_num"][forIndex],
  })
  forIndex += 1


# print(items_dict)

# ATTENTION! true & false should end up WITHOUT any (")
full_config = {
  "HorizonLayout": [
    {
      "layout": "logo",
      "showMenu": true,
      "showSearch": true,
      "showLogo": true,
      "menuIcon": {
        "name": "line_horizontal_3_decrease",
        "fontFamily": "CupertinoIcons"
      },
      "image": "https://i.imgur.com/LQWSjzt.png"
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
    },
    {
      "name": "מדפסות מעולות",
      "category": 2341,
      "layout": "threeColumn",
      "isSnapping": true
    }
  ],
  "Setting": {
    "MainColor": "#961b1e",
    "ProductListLayout": "list",
    "StickyHeader": true,
    "ProductDetail": "halfSizeImageType",
    "ShowChat": true,
    "FontFamily": "Heebo"
  },
  "TabBar": [
    {
      "layout": "home",
      "icon": "assets/icons/tabs/icon-home.png",
      "pos": 100,
      "key": "j3yj4st8gt"
    },
    {
      "layout": "search",
      "icon": "assets/icons/tabs/icon-search.png",
      "pos": 200,
      "key": "bzl41d82nk"
    },
    {
      "layout": "cart",
      "icon": "assets/icons/tabs/icon-cart2.png",
      "pos": 300,
      "key": "vxll1hkaq6"
    },
    {
      "layout": "profile",
      "icon": "assets/icons/tabs/icon-user.png",
      "showChat": true,
      "pos": 400,
      "settings": [
        "order",
        "wishlist",
        "darkTheme",
        "rating",
        "about"
      ],
      "background": "https://i.imgur.com/u2GRG8B.jpeg",
      "key": "mt0v8wv5c5"
    },
    {
      "layout": "wishlist",
      "icon": "assets/icons/tabs/icon-heartthin.png",
      "fontFamily": null,
      "showChat": false,
      "pos": 550
    }
  ],
  "Drawer": {
    "logo": null,
    "items": [
      {
        "type": "home",
        "show": false
      },
      {
        "type": "blog",
        "show": true
      },
      {
        "type": "login",
        "show": true
      },
      {
        "show": true,
        "type": "category"
      }
    ]
  },
  "VerticalLayout": {
    "key": "l7x7ddwj5q",
    "layout": "menu",
    "name": "המומלצים שלנו",
    "isVertical": true
  },
  "Version": 1,
  "Datetime": "15:24:04 - Mon 12 Jul"
}

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
print(full_config["HorizonLayout"])

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