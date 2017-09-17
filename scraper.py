import time
from query import Query
from process import Process
from random import randint

# application
if __name__ == "__main__":

    # Instantiate query class
    query = Query()
    # Instantiate Processing class
    process = Process()

    # Greet the user
    print("Enter number of entries to scrape. Default is 400 (40 pages).")
    total_entries = int(input("How many entries:"))
    # ToDo: error handling (everywhere)
    if not total_entries:
        total_entries = 400

    # starting at zero, increment by 10
    start = 0
    increment = 10

    # setup the file
    print("Enter file name for results, if it does not exist.")
    print("CSV only, format as filename.csv")
    filename = str.lower(input("Filename: "))

    if not filename:
        filename = "results.csv"

    path = "./" + filename

    # write headers first
    # ToDo: Allow user to set headers
    headers = ["Page Title", "Page Link", "Description"]
    process.write_csv(path, headers)

    # Prompt user for search terms
    terms = query.terms()
    # Generate URL
    url = query.url(terms)

    # process pages in batches of 10 - stop at 240
    while start <= total_entries:
        # grab 10 search results
        results = process.process_page(url, start)
        # process the list
        # break if none or no more results
        if not results:
            print("No more results.")
            break

        for child in results.children:
            # TODO: Use a dictionary
            # write 10 entries at a time, as opposed to writing row by row
            entry = process.create_entry(child)
            # write the row to CSV
            process.write_csv(path, entry)

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
