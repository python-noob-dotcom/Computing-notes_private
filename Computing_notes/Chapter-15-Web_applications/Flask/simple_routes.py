import flask


app = flask.Flask(__name__)

@app.route('/') # decoration, lowest level

def home():
    return 'Welcome to the home page'

@app.route('/test/readme.txt')
def home_2():
    return 'Please read this line of text'

if __name__ == '__main__':
    app.run(port = 5001)
