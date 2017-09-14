from bs4 import BeautifulSoup
import requests
import html5lib
import time
import csv
from random import randint


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
    data = [title, link, description]

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


def write_csv(data):
    with open(path, "w") as output_file:
        writer = csv.writer(output_file, delimiter=",")
        writer.writerow(data)


# application
if __name__ == "__main__":

    start = 0
    increment = 10
    count = 50
    path = "./results.csv"
    fields = ["Title", "Link", "Description"]
    # write headers
    write_csv(fields)
    # count = 250

    # process pages in batches of 10 - stop at 240
    while start != count:
        ol = process_page(start)
        # process the list
        for child in ol.children:
            # empty container for entries
            #entries = []
            entry = create_entry(child)

            #entries.append(entry)
            write_csv(entry)

        # set a random delay between 1 and 15 seconds
        delay = randint(1, 5)
        print("Pausing for {} Seconds".format(delay))
        time.sleep(delay)
        # increment counter
        start += increment
        print("Query complete")





