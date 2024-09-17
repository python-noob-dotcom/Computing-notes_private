import flask

app = flask.Flask(__name__, template_folder = './Task4_1')

@app.route('/')

def home():
    return flask.render_template('home.html')