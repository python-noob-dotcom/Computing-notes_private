import flask, sqlite3

app = flask.Flask(__name__, template_folder = 'TASK4_5')
driver_id = 1012

@app.route('/', methods = ['GET', 'POST'])

def home():
    return flask.render_template('index.html')

@app.route('/check', methods = ['POST'])

def check():
    global driver_id
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

@app.route('/rental', methods = ['POST'])

def rental():
    global driver_id
    date = flask.request.form['rental']
    vehicle = flask.request.form['vehicle']

    with sqlite3.connect(r'Computing-notes\Journey_to_A\Web_application\Web Applications Revision Practice 5\Taxi.db') as conn:
        cursor = conn.cursor()
        res = cursor.execute("SELECT * FROM Rent WHERE date = ? AND License = ?",
                        (date, vehicle)).fetchall()
        
        print(res)
        
        if res == []:
            message = 'Rental Successful'

            cursor.execute("INSERT INTO RENT (DriverID, License, Date, Paid) VALUES (?, ?, ?, 'No')",
                           (driver_id, vehicle, date))
            
            conn.commit()
        else:
            message = 'Vehicle Unavaliable for the selcted date'

        records = cursor.execute("SELECT Date, Model, Cost, Paid FROM Rent INNER JOIN Vehicle ON Rent.License = Vehicle.License WHERE DriverID = ?",
                                 (driver_id, )).fetchall()
        outstanding = cursor.execute("SELECT SUM(Cost) FROM Rent INNER JOIN Vehicle ON Rent.License = Vehicle.License WHERE DriverID = ?",
                                     (driver_id, )).fetchall()[0][0]

    return flask.render_template('rental.html', message = message, records = records, amount = outstanding)
        
    

if __name__ == '__main__':
    app.run(debug = True)