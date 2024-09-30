import flask, sqlite3

app = flask.Flask(__name__, template_folder= 'TASK4_4')

@app.route('/')

def home():
    with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\2024 ACJC Prelim\SUPERMARKET.db') as conn:
        cursor = conn.cursor()

        data = cursor.execute("""SELECT Customer.Name, Item.Name, Quantity
                              FROM (Item INNER JOIN Purchase
    ON Item.ItemID = Purchase.ItemID) AS A INNER JOIN Customer ON
    A.CustomerNumber = Customer.CustomerNumber WHERE DateTime LIKE '2024%' """).fetchall()
        
        return flask.render_template('home.html', data = data)
    
if __name__ == '__main__':
    app.run(debug = True)