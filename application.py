import json
import wikipedia
from flask import Flask

app = Flask(__name__)

@app.route('/')
def prompt():
    return 'Welcome! Please enter the term you would like to search for in the following URL >>> http://127.0.0.1:5000/[YOUR SEARCH TERM].wiki-search.com'

@app.route('/<search>.wiki-search.com')
def wiki_search(search):
    
    # When user follows the prompt message on landing page, it will route to a new page to call Python's Wikipedia library (module imported).
    
    url_dict = {'links': []}
    
    # New page is directed to display a dictionary of search results, which are dumped into a json (module imported).
    
    try:
        result = wikipedia.page(search, auto_suggest=False).url
        url_dict['links'].append(result)
        
    # Script uses try/except block for error handling.
        
    except wikipedia.DisambiguationError as e:
        for option in e.options:
            try:
                url = wikipedia.page(option.replace('"', ''), auto_suggest=False).url
                url_dict['links'].append(url)
                
                # For loop takes each url (result) and adds it to the end of the dictionary.
                
            except wikipedia.DisambiguationError:
                pass
            except wikipedia.PageError:
                return 'No page matches your search term. Please try searching for a different term.'
            
    return json.dumps(url_dict)

if __name__ == '__main__':
    app.run(debug=True)