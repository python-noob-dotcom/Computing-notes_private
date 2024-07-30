import flask, sqlite3

app = flask.Flask(__name__, template_folder = 'TASK4_3')

@app.route('/', methods = ['GET', 'POST'])

def home():
    return flask.render_template('index.html')

@app.route('/check', methods = ['GET', 'POST'])

def check():
    driver_id = int(flask.request.form['driver_id'])

    with sqlite3.connect(r'Computing-notes\Journey_to_A\Web_application\Web Applications Revision Practice 5\Taxi.db') as conn:
        cursor = conn.cursor()
        name = cursor.execute("SELECT Name FROM Driver WHERE ID = ?", (driver_id, )).fetchall()[0][0]
        vehicles = cursor.execute("SELECT License, Model, MaxPassenger FROM Vehicle").fetchall()
        for i in range(len(vehicles)):
            tag = ''
            for parameter in vehicles[i][:-1]:

                tag += str(parameter) + ', '
            tag +=  '(' + str(vehicles[i][-1]) + ' Passengers' + ')'
            vehicles[i] = tag

    return flask.render_template('booking.html', id= driver_id,  name = name, vehicles = vehicles)

if __name__ == '__main__':
    app.run(debug = True)