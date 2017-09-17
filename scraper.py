import requests
import html5lib
import time
import csv
from query import Query
from bs4 import BeautifulSoup
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


def process_page(page_number):
    # base url to start
    # base_url = "https://www.google.com/search?as_q=&as_epq=%22Dean+Klag%22" \
    #           "+site" \
    #           ":jhsph.edu&start="
    # url to target
    target_url = url + str(page_number)
    # get the page
    page = requests.get(target_url)
    # get html from the page
    soup = BeautifulSoup(page.text, "html5lib")
    # search results are in a div with ID of ires
    container = soup.find(id="ires")
    # and wrapped in an ordered list
    data = container.find("ol")
    return data


def write_csv(data):
    with open(path, "a") as output_file:
        writer = csv.writer(output_file, delimiter=",")
        writer.writerow(data)


# application
if __name__ == "__main__":

    print("Enter number of entries to scrape. Default is 400 (40 pages).")
    total_entries = int(input("How many entries:"))
    # ToDo: error handling (everywhere)
    if not total_entries:
        total_entries = 400

    start = 0
    increment = 10

    print("Enter file name for results, if it does not exist.")
    print("CSV only, format as filename.csv")
    filename = str.lower(input("Filename: "))

    if not filename:
        filename = "results.csv"

    path = "./" + filename
    # ToDo: Allow user to set headers
    headers = ["Page Title", "Page Link", "Description", "Action Needed",
               "Assigned To", "Completed"]
    # write headers
    write_csv(headers)

    # Instantiate query class
    query = Query()
    # Prompt user for search terms
    terms = query.terms()
    # Generate URL
    url = query.url(terms)

    # process pages in batches of 10 - stop at 240
    while start <= total_entries:
        # grab 10 search results
        results = process_page(start)
        # process the list
        for child in results.children:
            # TODO: Use a dictionary
            # write 10 entries at a time, as opposed to writing row by row
            entry = create_entry(child)
            # write the row to CSV
            write_csv(entry)

        print("{} entries processed and written to CSV.".format(start+10))

        # set a random delay between 1 and 3 seconds
        # so google doesn't think we are a bot
        delay = randint(1, 3)
        print("Pausing for {} Seconds".format(delay))
        time.sleep(delay)
        # increment counter
        start += increment

    print("{} total entries processed and written to CSV".format(start))
    print("Query Complete")
