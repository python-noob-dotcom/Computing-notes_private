import flask, sqlite3

app = flask.Flask(__name__)

@app.route('/')

# Task 4.3
def home():
    return flask.render_template('index.html')

# Task 4.4

@app.route('/arrivals')

def arrivals():
    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\JPJC Prelim 2024\Flight.db') as conn:
        cursor = conn.cursor()

        arrivals = cursor.execute('SELECT arrivalTime, departure, flightNum\
                       FROM Flight WHERE destination LIKE ?'
                       ('Singapore%', )).fetchall()
        
    return flask.render_template('arrivals.html', arrivals = arrivals)

# Task 4.5

@app.route('/departures')

def departures():
    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\JPJC Prelim 2024\Flight.db') as conn:
        cursor = conn.cursor()

        departures = cursor.execute('SELECT arrivalTime, destination, flightNum\
                       FROM Flight WHERE departure LIKE ?'
                       ('Singapore%', )).fetchall()
        
    return flask.render_template('departures.html', departures = departures)

# Task 4.6

@app.route('/query')

def query():
    return flask.render_template('query.html')

@app.route('/results', methods = ['POST'])

def results():
    flightnum = flask.request.form['flightNum']
    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\JPJC Prelim 2024\Flight.db') as conn:
        cursor = conn.cursor()

        departures = cursor.execute('SELECT *\
                       FROM Flight WHERE flightNum = ?'
                       (flightnum, )).fetchall()
        
    return flask.render_template('departures.html', departures = departures)
