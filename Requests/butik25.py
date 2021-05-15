from bs4 import BeautifulSoup, SoupStrainer
import requests, pickle
import json

session = requests.session()
global csrf_token

## Get pre-login cookies
def pre_login_cookies():
    global csrf_token
    response = session.get("https://members.lionwheel.com/?locale=he", data="")
    print(response.status_code)
    # print(response.cookies)
    # print(response.content)

    for element in BeautifulSoup(response.content,
                              # Element type like body, class..
                              parse_only=SoupStrainer('meta'),
                              features="html.parser"):
        # Attribute type (line) like </a>, </script>
        if element.has_attr("name") \
            and len(element["content"]) == 88:
            # Value in line like like href=, name=
            csrf_token = element["content"]
            break

    print(csrf_token)

    # Save cookies to file
    with open('butik25_Cookies', 'wb') as f:
        pickle.dump(session.cookies, f)

    # return response.cookies # No need

pre_login_cookies()

# try:
#     with open('butik25_Cookies', 'rb') as f:
#         session.cookies.update(pickle.load(f))
#     print("Pre-login cookies from file")
# except:
#     pre_login_cookies()
#     print("New pre-login cookies has created")
#
# session.post()