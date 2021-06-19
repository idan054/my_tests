import json
from pprint import pprint

x = """
{
  "status": "ok",
  "error_code": "",
  "data": [
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040985,
        "userid": 315628,
        "msg": "הוא ' 'שוב חזר",
        "time": "2021\\/06\\/19 ' '23:29:36",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:29:36",
        "active": true
      },
      "extra": {
        "hebrew_time": "55 ' 'שניות",
        "item_profile": {
          "nickname": "בודדה):",
          "anonflg": false,
          "active": true,
          "userid": 315628,
          "photostamp": "4875134152854",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040984,
        "userid": 309855,
        "msg": "Clancy",
        "time": "2021\\/06\\/19 ' '23:29:31",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:29:31",
        "active": true
      },
      "extra": {
        "hebrew_time": "1 ' 'דקות",
        "item_profile": {
          "nickname": "GOBLIN.",
          "anonflg": false,
          "active": true,
          "userid": 309855,
          "photostamp": "48114343254854",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040983,
        "userid": 112153,
        "msg": "\\"רוסיות\\\\בנות ' 'אליי\\" \\"מי באה\\" \\"מה מחפשת\\" \\"בנות תשלחו הודעה\\" \\"אמת או חובה\\" ' 'וכדומה, - אתם שום דבר.",
        "time": "2021\\/06\\/19 ' '23:29:30",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:29:30",
        "active": true
      },
      "extra": {
        "hebrew_time": "1 ' 'דקות",
        "item_profile": {
          "nickname": "JINKAZAMA",
          "anonflg": false,
          "active": true,
          "userid": 112153,
          "photostamp": "4888165651854",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040982,
        "userid": 113992,
        "msg": "יו ' 'יו\\nאני גבר ואני לא חרמן\\nאני טמבל ואני קצת ' 'שקרן\\nיו",
        "time": "2021\\/06\\/19 ' '23:29:27",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:29:27",
        "active": true
      },
      "extra": {
        "hebrew_time": "1 ' 'דקות",
        "item_profile": {
          "nickname": " ילד ' '-_-",
          "anonflg": false,
          "active": true,
          "userid": 113992,
          "photostamp": "4880142656854",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040981,
        "userid": 281515,
        "msg": "אין ' 'איך אני אוהב את אלה שאומרות שלחו ומסננות אין טין פשוט תמו ' 'ו",
        "time": "2021\\/06\\/19 23:29:14",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:29:14",
        "active": true
      },
      "extra": {
        "hebrew_time": "1 ' 'דקות",
        "item_profile": {
          "nickname": "my name ' 'is1",
          "anonflg": false,
          "active": true,
          "userid": 281515,
          "photostamp": "",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040980,
        "userid": 293598,
        "msg": "טוב ' 'סיימתי לכתוב את זה ועכשיו אני לא מספיקה לבכות.",
        "time": "2021\\/06\\/19 ' '23:29:07",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:29:07",
        "active": true
      },
      "extra": {
        "hebrew_time": "1 ' 'דקות",
        "item_profile": {
          "nickname": "Just Like ' 'You",
          "anonflg": false,
          "active": true,
          "userid": 293598,
          "photostamp": "48106217640854",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040979,
        "userid": 309469,
        "msg": "רונדו ' 'וזה",
        "time": "2021\\/06\\/19 ' '23:29:07",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:29:07",
        "active": true
      },
      "extra": {
        "hebrew_time": "1 ' 'דקות",
        "item_profile": {
          "nickname": "דויד ' 'בקהאם",
          "anonflg": false,
          "active": true,
          "userid": 309469,
          "photostamp": "47103305647854",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040977,
        "userid": 275440,
        "msg": "לא ' 'רוצה פחות אני שווה יותר",
        "time": "2021\\/06\\/19 ' '23:28:18",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:28:18",
        "active": true
      },
      "extra": {
        "hebrew_time": "2 ' 'דקות",
        "item_profile": {
          "nickname": "לא אכפת ' 'לי.",
          "anonflg": false,
          "active": true,
          "userid": 275440,
          "photostamp": "48106324754854",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040975,
        "userid": 315587,
        "msg": "יש ' 'פה דתיים\\/דתיות?",
        "time": "2021\\/06\\/19 ' '23:28:04",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:28:04",
        "active": true
      },
      "extra": {
        "hebrew_time": "2 ' 'דקות",
        "item_profile": {
          "nickname": "אח ' 'בלב12",
          "anonflg": false,
          "active": true,
          "userid": 315587,
          "photostamp": "",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040974,
        "userid": 307207,
        "msg": "בבקשה ' 'עזרה אני צריך עזרה",
        "time": "2021\\/06\\/19 ' '23:27:37",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:27:37",
        "active": true
      },
      "extra": {
        "hebrew_time": "2 ' 'דקות",
        "item_profile": {
          "nickname": "Mr. Jim ' 'Morrison",
          "anonflg": false,
          "active": true,
          "userid": 307207,
          "photostamp": "48110312141854",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040973,
        "userid": 287644,
        "msg": "איזה ' 'מציק",
        "time": "2021\\/06\\/19 ' '23:27:35",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:27:35",
        "active": true
      },
      "extra": {
        "hebrew_time": "2 ' 'דקות",
        "item_profile": {
          "nickname": " הקטנה של ' 'סטיפס",
          "anonflg": false,
          "active": true,
          "userid": 287644,
          "photostamp": "48100236557854",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040972,
        "userid": 263104,
        "msg": "סיפור ' 'למוצש\\nיצאתי לריצה, עם החולצה של הכושר קרבי. מסתבר שמאחורי רץ מישהו מגדסר ' 'נחל. אתם יודעים מה זה לרוץ כשרץ מאחוריכם לוחם סיירת? אני צריכה לעמוד בקצב ' 'שלו ולהראות שגם מלשבית יכולה. אל תשאלו מאיפה החשיבה הזו ' 'מגיעה",
        "time": "2021\\/06\\/19 ' '23:27:28",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:27:28",
        "active": true
      },
      "extra": {
        "hebrew_time": "3 ' 'דקות",
        "item_profile": {
          "nickname": "Cute ' 'girll",
          "anonflg": false,
          "active": true,
          "userid": 263104,
          "photostamp": "48117137664853",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040971,
        "userid": 265431,
        "msg": "אוף ' 'הרגשה חרא..",
        "time": "2021\\/06\\/19 ' '23:27:16",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:27:16",
        "active": true
      },
      "extra": {
        "hebrew_time": "3 ' 'דקות",
        "item_profile": {
          "nickname": "המלאכית ' 'בסגול",
          "anonflg": false,
          "active": true,
          "userid": 265431,
          "photostamp": "4766347460854",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040970,
        "userid": 227568,
        "msg": "4 ' 'ימים לחפשש",
        "time": "2021\\/06\\/19 ' '23:27:11",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:27:11",
        "active": true
      },
      "extra": {
        "hebrew_time": "3 ' 'דקות",
        "item_profile": {
          "nickname": "עומר(:",
          "anonflg": false,
          "active": true,
          "userid": 227568,
          "photostamp": "",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040969,
        "userid": 156179,
        "msg": "ואו ' 'כמעט חצי שנה לא הייתי פה",
        "time": "2021\\/06\\/19 ' '23:27:04",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:27:04",
        "active": true
      },
      "extra": {
        "hebrew_time": "3 ' 'דקות",
        "item_profile": {
          "nickname": "Princess ' 'Diana",
          "anonflg": false,
          "active": true,
          "userid": 156179,
          "photostamp": "49113124168853",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040968,
        "userid": 187078,
        "msg": "23:27 ' '\\n מישהו חושב עליי",
        "time": "2021\\/06\\/19 ' '23:26:45",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:26:45",
        "active": true
      },
      "extra": {
        "hebrew_time": "3 ' 'דקות",
        "item_profile": {
          "nickname": "הוקוס פוקוס תיחנקו ' 'מקוקוס.(בת)",
          "anonflg": false,
          "active": true,
          "userid": 187078,
          "photostamp": "4483132862854",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040967,
        "userid": 308480,
        "msg": "מה ' 'זה דסקורד איך שלא אומרים את זה ואיך כותבים את זה",
        "time": "2021\\/06\\/19 ' '23:26:18",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:26:18",
        "active": true
      },
      "extra": {
        "hebrew_time": "4 ' 'דקות",
        "item_profile": {
          "nickname": "Nam ' 'John",
          "anonflg": false,
          "active": true,
          "userid": 308480,
          "photostamp": "4763354146854",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040966,
        "userid": 263834,
        "msg": "אוף ' 'איך אני אוהבת גברים קשת ושור",
        "time": "2021\\/06\\/19 ' '23:26:04",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:26:04",
        "active": true
      },
      "extra": {
        "hebrew_time": "4 ' 'דקות",
        "item_profile": {
          "nickname": "מִיָה",
          "anonflg": false,
          "active": true,
          "userid": 263834,
          "photostamp": "48103233756854",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040964,
        "userid": 243707,
        "msg": "באמת ' 'קיימים אנשים שמתקשרים רק כדי לשאול מה שלומך",
        "time": "2021\\/06\\/19 ' '23:25:54",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:25:54",
        "active": true
      },
      "extra": {
        "hebrew_time": "4 ' 'דקות",
        "item_profile": {
          "nickname": "Not ' 'benas",
          "anonflg": false,
          "active": true,
          "userid": 243707,
          "photostamp": "5394345368853",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040963,
        "userid": 287022,
        "msg": "כאילו ' 'בא לי לעשות את האתגר הזה של הcopy me אבל עם הבעיות אמון שלי אני בחיים לא ' 'אפסיק גם אם יגידו שניצחתי",
        "time": "2021\\/06\\/19 ' '23:25:41",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:25:41",
        "active": true
      },
      "extra": {
        "hebrew_time": "4 ' 'דקות",
        "item_profile": {
          "nickname": "Chile anyways ' 'so",
          "anonflg": false,
          "active": true,
          "userid": 287022,
          "photostamp": "4864283857854",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040962,
        "userid": 286112,
        "msg": "שלחוו",
        "time": "2021\\/06\\/19 ' '23:25:02",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:25:02",
        "active": true
      },
      "extra": {
        "hebrew_time": "5 ' 'דקות",
        "item_profile": {
          "nickname": "לא להתאהב זה ' 'השטן!!!",
          "anonflg": false,
          "active": true,
          "userid": 286112,
          "photostamp": "4764357251854",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040961,
        "userid": 324232,
        "msg": "בבקשה ' 'דברו איתי (לא מי שמעל 15)",
        "time": "2021\\/06\\/19 ' '23:24:25",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:24:25",
        "active": true
      },
      "extra": {
        "hebrew_time": "6 ' 'דקות",
        "item_profile": {
          "nickname": "המכורה לסגול ' '(:",
          "anonflg": false,
          "active": true,
          "userid": 324232,
          "photostamp": "4862284148854",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040958,
        "userid": 262662,
        "msg": "כל ' 'כך הרבה חרמנים באמא שךי",
        "time": "2021\\/06\\/19 ' '23:23:50",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:23:50",
        "active": true
      },
      "extra": {
        "hebrew_time": "6 ' 'דקות",
        "item_profile": {
          "nickname": "Just average   ' '",
          "anonflg": false,
          "active": true,
          "userid": 262662,
          "photostamp": "52121316941853",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040957,
        "userid": 292531,
        "msg": "אני ' 'לא מצליחה להירדם . \\nטיפים ??",
        "time": "2021\\/06\\/19 ' '23:23:35",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:23:35",
        "active": true
      },
      "extra": {
        "hebrew_time": "6 ' 'דקות",
        "item_profile": {
          "nickname": " ' 'Simba",
          "anonflg": false,
          "active": true,
          "userid": 292531,
          "photostamp": "4892262151854",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040956,
        "userid": 280257,
        "msg": "לא ' 'זה \\nאש אש מדורה תחתונים של בחורה",
        "time": "2021\\/06\\/19 ' '23:23:16",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:23:16",
        "active": true
      },
      "extra": {
        "hebrew_time": "7 ' 'דקות",
        "item_profile": {
          "nickname": "~Chill~",
          "anonflg": false,
          "active": true,
          "userid": 280257,
          "photostamp": "4797245660854",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040955,
        "userid": 247019,
        "msg": "איך ' 'לעזאזל אנשים מחליטים שהם ביחד כשהם לא ראו אחד את השני אפילו פעם אחת ' 'ווטפ",
        "time": "2021\\/06\\/19 ' '23:23:09",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:23:09",
        "active": true
      },
      "extra": {
        "hebrew_time": "7 ' 'דקות",
        "item_profile": {
          "nickname": "Evolve",
          "anonflg": false,
          "active": true,
          "userid": 247019,
          "photostamp": "4875135849854",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040954,
        "userid": 277032,
        "msg": "איך ' 'נרדמים;-;",
        "time": "2021\\/06\\/19 ' '23:22:19",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:22:19",
        "active": true
      },
      "extra": {
        "hebrew_time": "8 ' 'דקות",
        "item_profile": {
          "nickname": "hello ' 'darkness",
          "anonflg": false,
          "active": true,
          "userid": 277032,
          "photostamp": "48103342957854",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040953,
        "userid": 263591,
        "msg": "אש ' 'אש מדורה\\nציצי ענק של בחורה",
        "time": "2021\\/06\\/19 ' '23:22:17",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:22:17",
        "active": true
      },
      "extra": {
        "hebrew_time": "8 ' 'דקות",
        "item_profile": {
          "nickname": "Broken!",
          "anonflg": false,
          "active": true,
          "userid": 263591,
          "photostamp": "4889308056854",
          "online": true
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040952,
        "userid": 324352,
        "msg": "כמה ' 'מין",
        "time": "2021\\/06\\/19 ' '23:22:12",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:22:12",
        "active": true
      },
      "extra": {
        "hebrew_time": "8 ' 'דקות",
        "item_profile": {
          "nickname": "All girls are the ' 'same",
          "anonflg": false,
          "active": true,
          "userid": 324352,
          "photostamp": "4875336653854",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    },
    {
      "objType": "penfriendsitem",
      "data": {
        "id": 5040951,
        "userid": 311078,
        "msg": "כתבו ' 'לי בקיר אכתוב לכם :)",
        "time": "2021\\/06\\/19 ' '23:22:06",
        "jumpcount": 0,
        "addtime": "2021\\/06\\/19 ' '23:22:06",
        "active": true
      },
      "extra": {
        "hebrew_time": "8 ' 'דקות",
        "item_profile": {
          "nickname": "בת אנוש ' 'נ=",
          "anonflg": false,
          "active": true,
          "userid": 311078,
          "photostamp": "4877122152854",
          "online": false
        }
      },
      "meta": {
        "active": true,
        "permissions": {
          "edit": false,
          "delete": false,
          "deleteWithoutMsg": false,
          "ban": false,
          "report": false,
          "showAdminMsgs": false,
          "itemOwner": false
        }
      }
    }
  ],
  "sqls": [
    {
      "source": "getObjectList",
      "exec_time": 0
    }
  ],
  "exec_time": "1031ms"
}
"""

pen_msgs = json.loads(x)
pprint(pen_msgs["data"][0]["data"]["userid"])
pprint(pen_msgs["data"][0]["data"]["msg"])
pprint(pen_msgs["data"][0]["extra"]["item_profile"]["nickname"])