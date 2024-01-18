from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

curr_dir = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(curr_dir, "invigilation.db")


@app.route('/')
def index():
    db = sqlite3.connect(db_file)
    query = """
    SELECT Name, Role, Count(Role)
    FROM Teacher, ExamDuty
    WHERE Teacher.TeacherID = ExamDuty.TeacherID
    GROUP BY Name, Role
    ORDER BY Name, Role
    """
    cursor = db.execute(query)
    records = cursor.fetchall()

    cursor.close()
    db.close()
    return render_template('index.html', records=records)


@app.route("/<name>/")
def schedule(name):
    db = sqlite3.connect(db_file)
    query = """
    SELECT SubjectName, PaperNo, Role, VenueName, Date, StartTime, EndTime
    FROM Teacher, Venue, ExamSession, ExamDuty
    WHERE Teacher.TeacherID = ExamDuty.TeacherID
    AND ExamSession.ExamSessionID = ExamDuty.ExamSessionID
    AND ExamSession.VenueID = Venue.VenueID
    AND Name = ?
    ORDER BY "Date" ASC, StartTime ASC
    """
    cursor = db.execute(query, (name,))
    records = cursor.fetchall()

    cursor.close()
    db.close()
    return render_template(
        'schedule.html',
        name=name,
        records=records)


if __name__ == '__main__':
    app.run(debug=False)
