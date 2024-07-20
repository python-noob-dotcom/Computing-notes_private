import flask, sqlite3
from flask import request

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def landing():
    if flask.request.method == 'GET':
        return flask.render_template('TASK4_3.html')
    
    if flask.request.method == 'POST':
        memID = flask.request.form['memID']
        compID = flask.request.form['compID']
        score = flask.request.form['score']
        request = "INSERT INTO Scores(Mem_ID, Comp_ID, Score) VALUES (?, ?, ?)"
        try:
            with sqlite3.connect(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 1\club.db') as conn:
                cursor = conn.cursor()
                cursor.execute(request, (memID, compID, int(score)))
                conn.commit()
            return 'Record Added Successfully'
        except sqlite3.Error as sql:
            return f'Ran into SQL error {sql}'
        except Exception as err:
            return f'Ran into exception. {err}'

if __name__ == '__main__':
    app.run(debug = True)
