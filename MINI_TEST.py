import json

x = """{ "HorizonLayout": [ { "layout": "logo", "showMenu": true, "showSearch": true, "showLogo": true, "menuIcon": { "name": "line_horizontal_3_decrease", "fontFamily": "CupertinoIcons" }, "image": "https://i.imgur.com/LQWSjzt.png" }, { "layout": "bannerImage", "isSlider": true, "autoPlay": true, "showNumber": false, "design": "default", "showBackGround": true, "radius": 8, "items": [ { "product": 25056, "image": "https://i.imgur.com/84ySdG3.jpg", "padding": 15.0 } ] }, { "layout": "bannerImage", "isSlider": true, "autoPlay": true, "showNumber": false, "design": "default", "showBackGround": true, "radius": 8, "items": [ { "category": 4783, "image": "https://i.imgur.com/H0bcI9u.jpg", "padding": 15.0 }, { "category": 2352, "image": "https://i.imgur.com/H7BJGsh.jpg", "padding": 15.0 } ] }, { "name": "מדפסות מעולות", "category": 2341, "layout": "threeColumn", "isSnapping": true } ], "Setting": { "MainColor": "#961b1e", "ProductListLayout": "list", "StickyHeader": true, "ProductDetail": "halfSizeImageType", "ShowChat": true, "FontFamily": "Heebo" }, "TabBar": [ { "layout": "home", "icon": "assets/icons/tabs/icon-home.png", "pos": 100, "key": "j3yj4st8gt" }, { "layout": "search", "icon": "assets/icons/tabs/icon-search.png", "pos": 200, "key": "bzl41d82nk" }, { "layout": "cart", "icon": "assets/icons/tabs/icon-cart2.png", "pos": 300, "key": "vxll1hkaq6" }, { "layout": "profile", "icon": "assets/icons/tabs/icon-user.png", "showChat": true, "pos": 400, "settings": [ "order", "wishlist", "darkTheme", "rating", "about" ], "background": "https://i.imgur.com/u2GRG8B.jpeg", "key": "mt0v8wv5c5" }, { "layout": "wishlist", "icon": "assets/icons/tabs/icon-heartthin.png", "fontFamily": null, "showChat": false, "pos": 550 } ], "Drawer": { "logo": null, "items": [ { "type": "home", "show": false }, { "type": "blog", "show": true }, { "type": "login", "show": true }, { "show": true, "type": "category" } ] }, "VerticalLayout": { "key": "l7x7ddwj5q", "layout": "menu", "name": "המומלצים שלנו", "isVertical": true }, "Version": 1, "Datetime": "15:24:04 - Mon 12 Jul" }"""
import json


json_object = json.loads(x)

# print(json.loads(x, indent=1))

# print(json.dumps(json_object))

print(json.dumps(json_object, indent=1, ensure_ascii=False))
