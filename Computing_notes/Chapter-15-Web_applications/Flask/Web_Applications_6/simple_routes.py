import flask


app = flask.Flask(__name__)

@app.route('/<name>') # decoration, lowest level

def home(name):
    return 'Welcome to the home page, ' + name

@app.route('/readme.txt')
def home_2():
    lines = []
    with open('./readme.txt') as f:
        lines = f.readlines()

    return lines

@app.route('/report')
def report():
    return 'This is a report'

@app.route('/render', methods = ['GET', 'POST'])

def render():
    if flask.request.method == 'POST':
        file = flask.request.form['filename']

        with open(file) as f:
            return f.readlines()
        
    return flask.render_template('test_render.html')

@app.route('/variable_routing/<s>')

def variable_routing(s):
    return 'You entered: ' + s

@app.route('/variable_routing/integer/<int:n>')

def var_routing_int(n):
    return 'You entered: ' + str(n)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
