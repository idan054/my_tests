import requests
from bs4 import BeautifulSoup, SoupStrainer
session = requests.session()

def get_links_from_tgSite():
    # Get response
    response = session.get("https://www.telegram-group.com/%d7%97%d7%93%d7%a9%d7%95%d7%aa/")
    print(response.status_code)

    # Get only links lines
    tg_lines = response.content.splitlines()
    tg_lines = filter(lambda _line: 'href="https://www.telegram-group.com/' in str(_line), tg_lines)

    # Remove any 'not link' parts from line
    tg_lines = list(map(lambda _line: str(_line).split(' href="')[1].split('"')[0]
                        # Split the line, get the After split value ([1]) X2
                        , tg_lines))

    # Translate חדשות in link
    tg_lines = list(
        map(lambda _line: str(_line).replace("https://www.telegram-group.com/%d7%97%d7%93%d7%a9%d7%95%d7%aa",
                                             "https://www.telegram-group.com/חדשות"), tg_lines))

    # Get only links from חדשות category
    finalLinks = list(filter(lambda _link: 'חדשות' in str(_link), tg_lines))
    finalLinks.remove("https://www.telegram-group.com/חדשות/page/2/")

    # print(*finalLinks, sep="\n")
    # print(len(finalLinks))
    return finalLinks

tg_links = get_links_from_tgSite()
# https://www.telegram-group.com/חדשות/%d7%a2%d7%95%d7%9c%d7%9d-%d7%94%d7%97%d7%93%d7%a9%d7%95%d7%aa-%d7%91%d7%98%d7%9c%d7%92%d7%a8%d7%9d/
response = session.get(tg_links[0])
print(response.status_code)
# print(response.content)

for link in BeautifulSoup(response.content, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        print(link['href'])
# for link in tg_links
