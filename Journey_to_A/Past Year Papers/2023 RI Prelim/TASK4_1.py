import flask 

app = flask.Flask(__name__, template_folder = 'TASK4_1')

@app.route('/')

def index():
    return flask.render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)