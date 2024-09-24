import flask, sqlite3

app = flask.Flask(__name__, template_folder = 'TASK4_2')

@app.route('/')

def index():
    return flask.render_template('home.html')

@app.route('/member')

def member():
    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\2023 RI Prelim\FITNESS.db') as conn:
        cursor = conn.cursor()

        query = """SELECT 
    Member.Name, 
    Member.Gender,
    Member.Age, 
    FitnessRecord.Height, 
    FitnessRecord.Weight, 
    FitnessRecord.WorkoutDate 
FROM 

Member LEFT OUTER JOIN 
    
    (FitnessRecord
INNER JOIN (
    SELECT MemberID, MAX(WorkoutDate) AS LatestWorkoutDate
    FROM FitnessRecord
    GROUP BY MemberID
) LatestRecord
    ON FitnessRecord.MemberID = LatestRecord.MemberID 
    AND FitnessRecord.WorkoutDate = LatestRecord.LatestWorkoutDate) AS A

    ON Member.MemberID = A.MemberID
ORDER BY 
    Member.Gender ASC, 
    Member.Name ASC;
"""

    data = cursor.execute(query).fetchall()

    return flask.render_template('details.html', data = data)

if __name__ == '__main__':
    app.run(debug = True)
