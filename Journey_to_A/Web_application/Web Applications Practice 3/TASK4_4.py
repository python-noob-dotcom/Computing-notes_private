import flask, sqlite3


query = " SELECT primary_sch, ?, ROUND(SUM(al) / ?, 2) FROM results INNER JOIN students \
    ON results.student_id = students.student_id WHERE primary_sch = ?"

with sqlite3.connect(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 3\ENROLMENT.db') as conn:
    cursor = conn.cursor()
    schools = list(set(\
        cursor.execute("SELECT primary_sch FROM students").fetchall()))
    data = []
    for school in schools:
        number_students = cursor.execute("SELECT COUNT(student_id) FROM students WHERE primary_sch = ?", school).fetchall()[0][0]
        data += cursor.execute(query, (int(number_students), int(number_students), school[0])).fetchall()
    data.sort(key= lambda x: x[0], reverse= False)


app = flask.Flask(__name__)

@app.route('/')

def home():
    return flask.render_template('display.html', data = data)

@app.route('/enrol', methods = ['POST'])

def enrol():
    cutoff = flask.request.form['cutoff']

    with sqlite3.connect(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 3\ENROLMENT.db') as conn:
        cursor = conn.cursor()

        student_ids = cursor.execute("SELECT student_id FROM students").fetchall()

        for student_id in student_ids:
            

if __name__ == '__main__':
    app.run(debug = True)