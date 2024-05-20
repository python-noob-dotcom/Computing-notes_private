import flask

from flask import url_for, render_template

app = flask.Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/greet/<name>/')

def greet(name):
    return render_template('greet.html', visitor=name)

if __name__ == '__main__':
    app.run(debug=True)