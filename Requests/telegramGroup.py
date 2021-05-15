from bs4 import BeautifulSoup, SoupStrainer
import datetime
import requests

## Get all Telegram t.me join links from telegram-group.com Category page

session = requests.session()

start_time = datetime.datetime.now()
print(start_time.strftime("%d/%m/%Y %H:%M:%S"))

def links_from_tgSite(category_page):
    # Get response
    _response = session.get(category_page)
    if _response.status_code != 200: print("STATUS CODE ERR ", _response.status_code)

    ## THE HARD WAY TO SCRAPE LINKS ##
    # ==================================
    # # Get only links lines
    # tg_lines = response.content.splitlines()
    # tg_lines = filter(lambda _line: 'href="https://www.telegram-group.com/' in str(_line), tg_lines)
    #
    # # Remove any 'not link' parts from line
    # tg_lines = list(map(lambda _line: str(_line).split(' href="')[1].split('"')[0]
    #                     # Split the line, get the After split value ([1]) X2
    #                     , tg_lines))

    ## THE EASY WAY TO SCRAPE LINKS ##
    # ==================================
    _tg_links = []
    for _link in BeautifulSoup(_response.content,
                               parse_only=SoupStrainer('a'),
                               features="html.parser"):
        if _link.has_attr('href'):
            # print(_link['href'])
            _tg_links.append(_link['href'])
    # print(*_tg_links, sep="\n")


    # Translate חדשות in link
    _tg_links = list(
        map(lambda _line: str(_line).replace("https://www.telegram-group.com/%d7%97%d7%93%d7%a9%d7%95%d7%aa",
                                             "https://www.telegram-group.com/חדשות"), _tg_links))

    # Get only links from חדשות category
    finalLinks = list(filter(lambda _link: 'חדשות' in str(_link), _tg_links))
    finalLinks.remove("https://www.telegram-group.com/חדשות/page/2/")

    # print(*finalLinks, sep="\n")
    print(f"{len(finalLinks)} Telegram news groups & channels found.")
    return finalLinks

tgSite_links = links_from_tgSite("https://www.telegram-group.com/%d7%97%d7%93%d7%a9%d7%95%d7%aa/")

def tgLinks_from_tgSite_links():
    telegram_links = []
    err_links = []
    product_link_counter = 1

    for product_link in tgSite_links:
        response = session.get(product_link)
        if response.status_code != 200:
            print(product_link_counter, "STATUS CODE ERR ", response.status_code)
            # print("Err Link is,", product_link)
            # err_links.append(product_link)
            # break

        for link in BeautifulSoup(response.content,
                                  parse_only=SoupStrainer('a'),
                                  features="html.parser"):
            if link.has_attr('href') \
                and "t.me" in link["href"]: # True / False  | is telegram link
                print(link['href'])
                telegram_links.append(link['href'])

    telegram_links = list(set(telegram_links)) # To remove duplicates
    return telegram_links

telegram_links = tgLinks_from_tgSite_links()

finish_time = datetime.datetime.now()
print(finish_time.strftime("%d/%m/%Y %H:%M:%S"))
run_time = finish_time - start_time
print("Overall it took", run_time.seconds, "seconds")

print(telegram_links)
print(len(telegram_links))