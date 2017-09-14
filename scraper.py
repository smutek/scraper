from bs4 import BeautifulSoup
import requests
import html5lib


def clean_link(link):
    clean = link.strip("/url?q=").split("&", 1)[0]
    return clean


def create_entry(html):
    # grab the title
    title = html.h3.text
    # grab the link
    href = html.a.get("href")
    link = clean_link(href)
    # returns with query strings on both ends, remove these
    # grab the description
    description = html.find('span', attrs={'class': 'st'}).text
    # stash the relevant bits in a dict
    data = {
        "Title": title,
        "Link": link,
        "Description": description,
        "Action Required": ""
    }
    return data


def process_page(start):
    # base url to start
    base_url = "https://www.google.com/search?as_q=&as_epq=%22Dean+Klag%22+site" \
           ":jhsph.edu&start="
    # url to target
    target_url = base_url + str(start)
    # get the page
    page = requests.get(target_url)
    # get html from the page
    soup = BeautifulSoup(page.text, "html5lib")
    # search results are in a div with ID of ires
    container = soup.find(id="ires")
    # and wrapped in an ordered list
    ol = container.find("ol")
    return ol


# application
if __name__ == "__main__":

    # increment in 10's  (stop at 240)
    start = 0
    increment = 10
    end = 240

    ol = process_page(start)
    # empty container for entries
    entries = []
    # process the list
    for child in ol.children:
        entry = create_entry(child)
    # add to entries list
        entries.append(entry)

    print(entries)
