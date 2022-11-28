from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/*.wiki-search')
def search():
    return render_template('home.html')

@app.route('/<search_term>.wiki-search')
def results():
    return render_template('index.html')

'''
@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        search_term = input('form.value')
        
        url = request.form['url']
    return render_template('index.html')
'''

if __name__ == '__main__':
    app.run(debug=True)    
    
# gets search term from user input from home search bar
# uses python input() method 
        # search_word = input('Search here!') --> or is there a different way to take the form input and insert it into the input()?
    # validates form input/data using WTForms (works with Flask)
    # assigns variable name to input as wildcard string literal?
    # takes user input (variable) and adds to next function/step
# inserts variable in app.route to make call (GET) using that endpoint (use CLI cURL to test)