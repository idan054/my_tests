import json

x = "Bruh4"
omniobj = json.loads("""{
    "data": {
        "msg": "PlaceHolder"
              },
      "objType": "penfriendsitem"
    }""")

print(omniobj)
omniobj["data"]["msg"] = "bruh5"
print(omniobj)
