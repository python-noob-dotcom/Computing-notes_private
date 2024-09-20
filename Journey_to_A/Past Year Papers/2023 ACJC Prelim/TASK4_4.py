import flask, sqlite3

app = flask.Flask(__name__, template_folder = './TASK4_4')

@app.route('/')

def home():
    return flask.render_template('home.html')

@app.route('/result', methods = ['POST'])

def res():
    compID = flask.request.form['compID']

    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\2023 ACJC Prelim\club.db') as conn:
        cursor = conn.cursor()

        query = 'SELECT Mem_Name, Members.Mem_ID, Comp_Score FROM Scores INNER JOIN Members \
            ON Scores.Mem_ID = Members.Mem_ID WHERE\
            Comp_ID = ? ORDER BY Comp_Score DESC'
        
        data = cursor.execute(query, (compID, )).fetchall()

    return flask.render_template('result.html', data = data)

if __name__ == '__main__':
    app.run(debug = True)