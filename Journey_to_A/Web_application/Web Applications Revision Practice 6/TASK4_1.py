import flask, sqlite3

app = flask.Flask(__name__, template_folder = './templates')

@app.route('/')

def index():
    return flask.render_template('index.html')

@app.route('/details')

def details():

    query = """
            SELECT Name, Gender, Age, Weight, Height, WorkoutDate FROM Member 
    LEFT OUTER JOIN FitnessRecord ON Member.MemberID = FitnessRecord.MemberID
    ORDER BY Gender
            """
    
    with sqlite3.connect(r'Computing-notes\Journey_to_A\Web_application\Web Applications Revision Practice 6\FITNESS.db') as conn:
        cursor = conn.cursor()

        details = cursor.execute(query).fetchall()

    return flask.render_template('details.html', member_details = details)

@app.route('/stats')

def stats():
    with sqlite3.connect(r'Computing-notes\Journey_to_A\Web_application\Web Applications Revision Practice 6\FITNESS.db') as conn:
        cursor = conn.cursor()

        res = cursor.execute('SELECT Gender, COUNT(Member.MemberID), ROUND(AVG(Age), 1), \
                             ROUND(AVG(Weight), 1), ROUND(AVG(Height), 1) FROM Member \
                            LEFT OUTER JOIN FitnessRecord ON Member.MemberID = FitnessRecord.MemberID\
                            GROUP BY Gender ORDER BY WorkoutDate').fetchall()
        
    return flask.render_template('stats.html', binary = res)

        

if __name__ == '__main__':
    app.run(debug = True)