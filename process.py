import requests
import html5lib
import csv
from bs4 import BeautifulSoup


class Process:
    def clean_link(self, link):
        clean = link.strip("/url?q=").split("&", 1)[0]
        return clean

    def create_entry(self, html):
        # grab the title
        title = html.h3.text
        # grab the link
        href = html.a.get("href")
        link = self.clean_link(href)
        # returns with query strings on both ends, remove these
        # grab the description
        description = html.find('span', attrs={'class': 'st'}).text
        # stash the relevant bits in a dict
        data = [title, link, description]
        return data

    def process_page(self, url, page_number):
        start = "&start=" + str(page_number)
        # url to target
        target_url = url + start
        # get the page
        page = requests.get(target_url)
        # get html from the page
        soup = BeautifulSoup(page.text, "html5lib")
        # search results are in a div with ID of ires
        container = soup.find(id="ires")
        # and wrapped in an ordered list
        data = container.find("ol")
        return data

    def write_csv(self, path, data):
        with open(path, "a") as output_file:
            writer = csv.writer(output_file, delimiter=",")
            writer.writerow(data)
