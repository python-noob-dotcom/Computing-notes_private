import sqlite3, flask

app = flask.Flask(__name__)

@app.route('/')

def landing():
    return flask.render_template('TASK4_4.html')

@app.route('/result', methods = ['POST'])

def result():
    Comp_ID = flask.request.form['Comp_ID']
    query = "SELECT Members.Mem_Name, Members.Mem_ID, Scores.Score FROM Members INNER JOIN Scores on Members.Mem_ID = Scores.Mem_ID WHERE Comp_ID = ? ORDER BY Score DESC"

    with sqlite3.connect(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 1\club.db') as conn:
        cursor = conn.cursor()

        res = cursor.execute(query, (Comp_ID,)).fetchall()

    return flask.render_template('TASK4_4_result.html', result = res)

if __name__ == '__main__':
    app.run(debug = True)

