import flask, sqlite3 

app = flask.Flask(__name__, template_folder = 'TASK4_4')

@app.route('/')

def home():
    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\2023 RVHS Prelim\ENROLMENT.db') as conn:
        cursor = conn.cursor()

        data = cursor.execute("""SELECT primary_sch, COUNT(DISTINCT results.student_id), ROUND(AVG(results.al * 4), 2)
FROM results INNER JOIN students ON results.student_id = students.student_id
GROUP BY primary_sch ORDER BY primary_sch DESC""").fetchall()
        
    return flask.render_template('home.html', data = data)

@app.route('/res', methods = ['POST'])

def res():
    cutoff = flask.request.form['cutoff']

    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\2023 RVHS Prelim\ENROLMENT.db') as conn:
        cursor = conn.cursor()
        
        data = cursor.execute(
            """
SELECT stu_name, gender, primary_sch, SUM(results.al) AS ttl, guardian_name, 
guardian_email FROM 
(results INNER JOIN students on results.student_id = 
students.student_id) AS A INNER JOIN guardians ON A.guardian_id = guardians.guardian_id
GROUP BY students.student_id
HAVING ttl < ?
ORDER BY primary_sch DESC, ttl ASC 
            """
        , (int(cutoff), )).fetchall()

    return flask.render_template('results.html', data = data)

if __name__ == '__main__':
    app.run(debug = True)