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
</div>
```

Use requests to fetch the page, html5lib to parse, and BS4 to extract the info.
Use CSV to write to CSV.

##Requires 
- BeautifulSoup4
- html5lib

## ToDo 
- Build the loop & counter
- Output to CSV
- Clean up


