import flask, sqlite3

app = flask.Flask(__name__, template_folder= './TASK4_4')

@app.route('/')

def home():
    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\2022 A level\LIBRARY.db') as conn:
        cursor = conn.cursor()

        res = cursor.execute('SELECT FamilyName, GivenName, Title FROM Member INNER JOIN (Loan INNER JOIN Book ON Loan.BookID = Book.BookID) ON Loan.MemberNumber = Member.MemberNumber WHERE Returned = "FALSE"').fetchall()

    return flask.render_template('index.html', results = res)

if __name__ == '__main__':
    app.run(debug = True)