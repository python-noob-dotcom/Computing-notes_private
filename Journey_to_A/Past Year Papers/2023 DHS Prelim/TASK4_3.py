import flask, sqlite3

app = flask.Flask(__name__, template_folder = 'TASK_4_web')

@app.route('/')

def home():
    return flask.render_template('home.html')

@app.route('/count')

def count():
    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\2023 DHS Prelim\election.db') as conn:
        cursor = conn.cursor()

        data = cursor.execute("""
SELECT Candidate.Name, Candidate.Class, COUNT(VID) AS ttl FROM Candidate INNER JOIN Vote
ON Candidate.CID = Vote.CID GROUP BY Candidate.CID ORDER BY ttl DESC
                              """).fetchall()
        
    return flask.render_template('count.html', data = data)

@app.route('/breakdown', methods = ['GET', 'POST'])

def breakdown():
    if flask.request.method == 'GET':
        return flask.render_template('votebreakdown.html', data = None)
    
    else:
        name = flask.request.form['opt']

        with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\2023 DHS Prelim\election.db') as conn:
            cursor = conn.cursor()

            data = cursor.execute("""
SELECT Voter.Name, Voter.Class, Candidate.Name AS ttl FROM (Candidate INNER JOIN Vote
ON Candidate.CID = Vote.CID ) AS A INNER JOIN Voter ON A.VID = Voter.VID WHERE Candidate.Name = ?""", (name, )).fetchall()
            
        return flask.render_template('votebreakdown.html', data = data)


if __name__ == '__main__':
    app.run(debug = True)