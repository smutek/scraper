from bs4 import BeautifulSoup
import requests
import html5lib

# base url to start
base_url = "https://www.google.com/search?as_q=&as_epq=%22Dean+Klag%22+site" \
           ":jhsph.edu&start="
# increment in 10's  (stop at 240)
start = 0
# url to target
target_url = base_url + str(start)
# get the page
page = requests.get(target_url)
# get html from the page
soup = BeautifulSoup(page.text, "html5lib")
# search results are in a div with ID of ires
container = soup.find(id="ires")
# and wrapped in an ordered list
list = container.find("ol")
# empty container for entries
entries = []
# process the list
for child in list.children:
    # grab the title
    title = child.h3.text
    # grab the link
    href = child.a.get("href")
    # returns with query strings on both ends, remove these
    link = href.strip("/url?q=").split("&", 1)[0]
    # grab the description
    description = child.find('span', attrs={'class': 'st'}).text
    # stash the relevant bits in a dict
    entry = {
        "Title": title,
        "Link": link,
        "Description": description,
        "Action Required": ""
    }
    # add to entries list
    entries.append(entry)

print(entries)
