import csv
from urllib.parse import urlparse

"""
Save 1 CSV with all results, 
remove description field,
break URL down up to 3 levels deep
fields: 
page title
page link
level 1 (ie. research)
level 2 (ie. centers and institutes)
level 3 (ie. some center name)

save to new csv 
"""

# application
if __name__ == "__main__":

    # open/create files
    old_file = './coa.csv'
    new_file = './coa_sorted.csv'

    # write headers to new file
    with open(new_file, "a") as output_file:
        fieldnames = ['Page Title', 'Page Link', 'Level 1', 'Level 2', 'Level 3']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

    # open old file
    with open(old_file, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        # loop through records
        for row in reader:
            title = row['Page Title']
            link = row['Page Link']
            # strip the path out of the url
            parse = urlparse(row['Page Link'])
            path = parse.path
            # split url: foo/bar => foo bar
            segments = path.split('/')

            # this is so inefficient but I am tired
            # try to assign segments, assign null if not
            try:
                level_1 = segments[1]
            except IndexError:
                level_1 = 'null'
            try:
                level_2 = segments[2]
            except IndexError:
                level_2 = 'null'
            try:
                level_3 = segments[3]
            except IndexError:
                level_3 = 'null'

            # write the new row to the new file
            with open(new_file, "a") as output_file:
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                writer.writerow({'Page Title': title,
                                 'Page Link': link,
                                 'Level 1': level_1,
                                 'Level 2': level_2,
                                 'Level 3': level_3,
                                 })
