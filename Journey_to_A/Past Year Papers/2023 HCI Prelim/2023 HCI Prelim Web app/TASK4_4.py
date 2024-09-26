import flask, sqlite3

app = flask.Flask(__name__)

@app.route('/')

def index():
    return flask.render_template('index.html')

@app.route('/results', methods = ['POST'])

def results():
    date = flask.request.form['date']

    with sqlite3.connect(r'Computing-notes\Journey_to_A\Web_application\Web Applications Revision Practice 7\store.db') as conn:
        cursor = conn.cursor()

        query = "SELECT DonutName, Quantity FROM Sale INNER JOIN Donut ON Sale.DonutID = Donut.DonutID\
              WHERE Date = ? GROUP BY DonutName ORDER BY Quantity DESC "
        
        results = cursor.execute(query, (date, )).fetchall()

    return flask.render_template('result.html', results = results)

if __name__ == '__main__':
    app.run(debug = True)