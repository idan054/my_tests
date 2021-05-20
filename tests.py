import pickle
from pprint import pprint

# with open('../config/post-login_butik25_Cookies', 'rb') as f:
with open('config/post-login_butik25_Cookies', 'rb') as f:
    x = pickle.load(f)
    # pprint(x)

# _cookie = session.cookies.values()
_cookie = x.values()
print(len(_cookie))
_cookie = x.keys()
print(_cookie)
# open("../config/stips_Cookies.txt", "w").write(_cookie[0])  # Overwrite
# open("../config/stips_Cookies.txt", "a").write(f"\n{_cookie[1]}")  # adds to file
