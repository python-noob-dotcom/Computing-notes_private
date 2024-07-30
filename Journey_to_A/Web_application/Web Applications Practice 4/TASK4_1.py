import flask, sqlite3

app = flask.Flask(__name__)

@app.route('/')

def home():
    with sqlite3.connect(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 4\TASK4.db') as conn:
        cursor = conn.cursor()
        query = 'SELECT name, artist, type FROM Event'

        data = cursor.execute(query).fetchall()

        return flask.render_template('TASK4_1.html', data = data)
    
@app.route('/<event>')

def see_dates(event):
    with sqlite3.connect(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 4\TASK4.db') as conn:
        cursor = conn.cursor()
        if 'GARN' in event:
            event = 'GARN%'
        elif 'JACK' in event:
            event = 'JACK%'
        elif 'Legend' in event:
            event = 'Legend%'
        elif 'Taylor' in event:
            event = 'Taylor%'
        else:
            return "Invalid Event Selected"

    data = cursor.execute("SELECT date, time, venue FROM TimeTable INNER JOIN \
                          EVENT ON TimeTable.event_id = Event.ID WHERE Event.name LIKE ?",  (event, )).fetchall()

    name_of_event = cursor.execute("SELECT name FROM Event WHERE name LIKE ?", (event, )).fetchall()[0][0]

    return flask.render_template('TASK4_1_2.html', data = data, name_of_event = name_of_event)

if __name__ == '__main__':
    app.run(debug = True)