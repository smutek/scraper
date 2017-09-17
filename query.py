"""
front: https://www.google.com/search?
All: as_q=All+these+words
Exact: as_epq=%22Exact+Phrase
Any: as_oq=Any+here
None: as_eq=None+This
Site: as_sitesearch=smutek.net
Empty queries get passed in without value
sep query strings with &

end of query
these params are appended by default, not sure what as_occt is
&as_occt=any&safe=images&as_filetype=&as_rights=
"""


class Query:
    def __init__(self):

        self.front = "https://www.google.com/search?"

        self.params = {
            "as_q=": "",  # term+term
            "&as_epq=": "",  # exact %22term+term%22
            "&as_oq=": "",  # term+term
            "&as_eq=": "",  # none term+term
            "&as_sitesearch=": ""
        }

        self.prompts = {
            "as_q=": "All of these terms: ",  # term+term
            "&as_epq=": "This exact term or phrase: ",  # exact %22term+term%22
            "&as_oq=": "Any of these terms: ",  # term+term
            "&as_eq=": "None of these terms: ",  # none term+term
            "&as_sitesearch=": "Search this site:"
        }

        self.tail = "&as_occt=any&safe=images&as_filetype=&as_rights="

    # prompt the user for query terms
    def terms(self):

        print("Enter terms. Separate multiple values with space.")
        print("Press enter to skip.")

        for key, value in self.prompts.items():

            # prompt user

            terms = str(input(value))

            # if user has entered terms
            if terms:
                # replace spaces with plus
                terms = terms.replace(" ", "+")
                # if exact match param, wrap in %22
                if key == "&as_epq=":
                    terms = "%22" + terms + "%22"

            self.params[key] = terms

        return self.params

    # construct query string
    def url(self, dictionary):

        url = self.front
        for key, value in dictionary.items():
            param = key + value
            url += param
        url += self.tail

        return url
