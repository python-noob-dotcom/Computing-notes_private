import flask
from flask import url_for, render_template
import sqlite3

app = flask.Flask(__name__)
@app.route('/')

def landing():
    erroneous = url_for("delete_erroneous_certs")
    vip = url_for("vip_voucher_recepients")
    cert = url_for("add_certificate")

    return render_template('render.html', erroneous = erroneous, vip = vip, add_record = cert)

@app.route('/delete_erroneous_certs')

def delete_erroneous_certs():
    with sqlite3.connect('insert_db_here') as conn:
        cursor = conn.cursor()

        count = cursor.execute('SELECT * FROM Certificate WHERE status = "404"')
        result = cursor.execute('DELETE FROM Certificate WHERE status = "404"')

        conn.commit()

        return f'Deleted erroneous certificates, the number of erroneous certificates are {count.rowcount}'
    
@app.route('/vip_voucher_recepients')

def vip_voucher_recepients():
    with sqlite3.connect('insert_db_here') as conn:
        cursor = conn.cursor()

        vips = cursor.execute("SELECT * FROM Certificate INNER JOIN Member INNER JOIN Course ON Certificate.MemberID = Member.MemberID AND Certificate.CourseCode = Course.CourseCode \
                                WHERE Certificate.IssueDate > '2023-01'")
        
        result = vips.fetchall()
        
        return render_template('vip.html', result = result)
    
@app.route('/certificates', methods = ['GET', 'POST'])

def add_certificate():

    if flask.request.method == 'GET':
        return render_template('cert_record.html')
    
    id = flask.request.form['MemberID']
    code = flask.request.form['CourseCode']
    date = flask.request.form['Date']

    try:
        with sqlite3.connect('insert_db_here') as conn:
            cursor = conn.cursor()

            cursor.execute('INSERT INTO Certificate VALUES (?, ?, ?, "200")', (id, code, date))
            conn.commit()

        return f'Insertion Successful, Details: ID = {id}, Course Code = {code}, Issue Date = {date}'
    except:
        return 'Insertion unsuccessful'

if __name__ == '__main__':
    app.run(port = 5000, debug = True)


    