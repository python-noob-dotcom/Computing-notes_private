import flask

app = flask.Flask(__name__, template_folder = 'TASK4_2')

@app.route('/', methods = ['GET', 'POST'])

def home():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')
    else:
        return 'Booked'
    
if __name__ == '__main__':
    app.run(debug = True)