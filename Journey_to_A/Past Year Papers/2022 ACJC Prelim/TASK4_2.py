import flask, sqlite3

app = flask.Flask(__name__, template_folder = 'TASK4_2')

@app.route('/')

def home():
    return flask.render_template('home.html')

@app.route('/insert')

def insert():
    return flask.render_template('insert.html')

@app.route('/res', methods = ['POST'])

def res():
    bID = flask.request.form['bID']
    title = flask.request.form['title']
    price = flask.request.form['price']
    quan = flask.request.form['quan']

    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\2022 ACJC Prelim\Task4.db') as conn:
        cursor = conn.cursor()

        cursor.execute('BEGIN TRANSACTION')

        try:
            cursor.execute('INSERT INTO books VALUES (?, ?, ?)', (bID, title, price))
        except sqlite3.Error: # means that the book is already existing, so will return unique constrained fail
            pass

        for i in range(int(quan)):
            cursor.execute(
                'INSERT INTO copies VALUES (?, ?)'
            , (f'000{i}', bID))

        conn.commit()

    return 'Insertion successful'

@app.route('/display')

def display():
    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\2022 ACJC Prelim\Task4.db') as conn:
        cursor = conn.cursor()

        data = cursor.execute("""
SELECT books.bookID, books.price, books.title, SUM(copyID)
FROM books INNER JOIN copies ON books.bookID = copies.bookID
GROUP BY books.bookID ORDER BY books.title
""").fetchall()
        
    
    return flask.render_template('display.html', data = data)

if __name__ == '__main__':
    app.run(debug = True)

