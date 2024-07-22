import flask, sqlite3

app = flask.Flask(__name__)

@app.route('/')

def landing():
    return flask.render_template('home.html')

@app.route('/purchasing', methods = ['POST'])


def purchase():
    query = "SELECT * FROM Ticket WHERE Ticket.Date LIKE ?"
    month = flask.request.form['month']

    with sqlite3.connect(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 2\MerlionThemePark.db') as conn:
        cursor = conn.cursor()

        result = cursor.execute(query, (f'%{month}%',)).fetchall()

    return flask.render_template('ticket.html', result = result)

@app.route('/transaction', methods = ['POST'])

def transaction_confirm():
    month = flask.request.form['month']
    day = flask.request.form['day']
    quantity = flask.request.form['quantity']

    with sqlite3.connect(r'C:\Users\eugen\Desktop\Computing_notes\Computing-notes\Journey_to_A\Web_application\Web Applications Practice 2\MerlionThemePark.db') as conn:
        cursor = conn.cursor()

        qty_avail, unitPrice = cursor.execute("SELECT availQuan, unitPrice FROM Ticket WHERE Date LIKE ?", (f'%{month}-{day}',)).fetchone()

        if qty_avail > int(quantity):
            cursor.execute("INSERT INTO Sale(tDate, quan, totalPrice) VALUES (?, ?, ?)", (f'2023-{month}-{day}', int(quantity), int(quantity) * int(unitPrice)))
            cursor.execute("UPDATE Ticket Set availQuan = availQuan - ? WHERE DATE LIKE ?", (int(quantity), f'%{month}-{day}'))

            conn.commit()
            message = f'You have purchased {quantity} tickets for {month}-{day}'
            return flask.render_template('transaction.html', message= message)
        else:
            message = None
            return flask.render_template('transaction.html', message = message)
        
if __name__ == '__main__':
    app.run(debug = True)
