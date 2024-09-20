import flask, sqlite3

app = flask.Flask(__name__, template_folder= './TASK4_3')

@app.route('/')

def home():
    return flask.render_template('home.html')

@app.route('/result', methods = ['POST'])

def add():
    compID = flask.request.form['compID']
    memID = flask.request.form['memID']
    score = flask.request.form['score']

    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\2023 ACJC Prelim\club.db') as conn:
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Scores VALUES (?, ?, ?)", (compID, memID, score))
        conn.commit()

    return 'Insertion Complete'

if __name__ == '__main__':
    app.run(debug = True)