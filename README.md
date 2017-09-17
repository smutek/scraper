# List of Links Super Scraper Maker

Turn some Google search results into a list that can be exported to CSV &
imported to Google Docs or Excel or something. 

Pass a search string in, get a page (10 results), and pull the needed info. 
Increment a counter as needed to get the next page of results. Rinse & repeat.
 
 Google search results live in a structure something like:
 
 ```html
<div>
<-- lots of stuff -->
    <div id="ires">
        <ol>
            <!-- Div with Result -->
            <!-- Div with Result -->
            <!-- Div with Result -->
        </ol>
    </div>
<-- lots of stuff -->
</div>
```

Use requests to fetch the page, html5lib to parse, and BS4 to extract the info.
Use CSV to write to CSV.

## Requires
- Python 3
- BeautifulSoup4
- html5lib
- Requests

## To use

Assumes you have python3 installed, along with pip3.

- Install requirements however you see fit. I use a virtualenv
- Use `python3 scraper.py`
- Follow the prompts

## ToDo
- Error handling (there is very little)
- Clean up

## Notes

Note that there's no error checking to speak of. I wrote this mainly for my own use,
 so use at yer own risk, ye'r on yer own - though if you know how to use this
 I dare say you probably know of another better faster way to do what this does. :)
  
  Regardless, this was fun. I really like Python.

